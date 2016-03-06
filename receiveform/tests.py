from django.test import TestCase

# Create your tests here.
from receiveform.models import UserEntity




class UserEntityTest(TestCase):

    def setUp(self):
        self.user =UserEntity(email="test@gmail.com")
        self.user.save()


    def test_user_email(self):
        self.assertEqual(self.user.email,"test@gmail.com")


    def test_user_token(self):
        self.assertEqual(len(self.user.public_key),36)
        self.assertEqual(len(self.user.private_key),36)

    def test_duplicate_user(self):
        self.assertEqual(UserEntity.is_present("test@gmail.com"),True)

    def test_new_user(self):
        self.assertEqual(UserEntity.is_present("new@gmail.com"),False)

