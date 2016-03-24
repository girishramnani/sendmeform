from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from uuid import UUID
# Create your views here.
from django.views.generic.base import TemplateView, View, RedirectView
from falcon.status_codes import HTTP_500

from receiveform.models import UserEntity, DataStore
from receiveform.tasks import mock_send_mail
import json


class Index(TemplateView):

    template_name = "index.html"

    def post(self,request,*args,**kwargs):

        email = request.POST['email']

        if UserEntity.is_present(email):
            messages.add_message(request,messages.ERROR,"That email already exists.")
            return redirect(reverse("index"))
        else:
            user = UserEntity(email=email)
            user.save()
            mock_send_mail(user)
            messages.add_message(request,messages.SUCCESS,"Thank you for signing Up")
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)


class ClientDashBoard(TemplateView):


    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):

        # test token : 8ce853f33e07426d9b21ec5b2c51b465d
        context = self.get_context_data(**kwargs)
        try:
            private_token = self.kwargs['token']
            current_user = UserEntity.objects.get(private_key=private_token)
        except (ObjectDoesNotExist,ValueError) as e:
            raise Http404("User token is invalid")
        context["user"] = current_user
        context["datastore"] = current_user.datastore_set.order_by("-created_on")

        return self.render_to_response(context)



class ClientFormEndpoint(RedirectView):


    pattern_name = "fallbackRedirect"

    def get(self, request, *args, **kwargs):
        return HttpResponse("Unsupported Method")

    def post(self,request,*args,**kwargs):
        public_token = kwargs['public_token']
        try:
            user = UserEntity.objects.get(public_key=public_token)
        except ObjectDoesNotExist:
            raise Http404("This user doesnt not exist")

        json = request.POST.dict()
        try:
            data = DataStore(user=user,data=json)
            data.save()
        except Exception as e:

            return HttpResponse("There was something wrong with the server",status=HTTP_500)

        return redirect(self.get_redirect_url())







