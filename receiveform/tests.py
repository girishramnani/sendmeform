from django.core.urlresolvers import reverse
from django.template.base import Template
from django.template.context import Context
from django.test import TestCase

# Create your tests here.
from receiveform.models import UserEntity
from django.test import Client



class UserEntityTest(TestCase):

    def setUp(self):
        self.user =UserEntity(email="test@gmail.com")
        self.user.save()


    def test_user_email(self):
        self.assertEqual(self.user.email,"test@gmail.com")


    def test_user_token(self):
        self.assertEqual(len(self.user.public_key),32)
        self.assertEqual(len(self.user.private_key),32)

    def test_duplicate_user(self):
        self.assertEqual(UserEntity.is_present("test@gmail.com"),True)

    def test_new_user(self):
        self.assertEqual(UserEntity.is_present("new@gmail.com"),False)

    def tearDown(self):
        self.user.delete()


class ClientEndpointTest(TestCase):


    def setUp(self):
        self.user = UserEntity(email="test@gmail.com")
        self.user.save()
        self.public_token = self.user.public_key


    def test_data_send_default_page(self):

        client = Client()
        endpoint = reverse("endpoint",kwargs={'public_token':self.public_token})
        resp = client.post(endpoint,{'name':self.public_token})
        response_template = client.get(resp.url)


        template = Template(open("templates/default_redirect_page.html").read())
        context =Context({'hello':'world'})

        self.assertEqual(template.render(context),response_template.rendered_content)



