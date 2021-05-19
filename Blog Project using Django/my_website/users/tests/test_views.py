from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from users.views import register, profile
from users.models import Profile
from mixer.backend.django import mixer
from users.models import Profile
import json


class TestViews(TestCase):
    
    def test_project_register_authenticated(self):
        path = reverse('register')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        response = register(request)
        assert response.status_code == 200

   

    

