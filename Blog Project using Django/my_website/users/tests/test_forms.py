from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.forms import UserUpdateForm, ProfileUpdateForm


class TestForms(TestCase):

    def test_registration_valid_data(self):
        form = UserCreationForm(data={
            'username':'me',
            'email':'me@test.com',
            'password1':'awE64Gjdldl8DJKH',
            'password2':'awE64Gjdldl8DJKH'
        })

        self.assertTrue(form.is_valid())

    def test_registration_empty(self):
        form = UserCreationForm(data={})
        self.assertFalse(form.is_valid())
         
        





