from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail

# Create your views here.
from django.views.generic.base import TemplateView, View

from receiveform.models import UserEntity
from receiveform.tasks import mock_send_mail


class Index(TemplateView):

    template_name = "index.html"


    def post(self,request,*args,**kwargs):

        email = request.POST['email']
        if UserEntity.is_present(email):
            print("already present")
            return redirect(reverse("index"))
        else:
            user = UserEntity(email=email)

            mock_send_mail(user)

            user.save()
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)


class ClientDashBoard(TemplateView):


    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):

        private_token = self.kwargs['token']
        current_user = get_object_or_404(UserEntity,private_key = private_token)
