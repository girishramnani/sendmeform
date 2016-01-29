
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
from django.views.generic.base import TemplateView, View



class Index(TemplateView):

    template_name = "index.html"


    def post(self,request,*args,**kwargs):

        email = request.POST['email']
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)