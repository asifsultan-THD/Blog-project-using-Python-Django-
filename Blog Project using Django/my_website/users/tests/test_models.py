from django.test import TestCase
from users.models import Profile
from django.contrib.auth.models import User

class TestModels(TestCase):

    def test_project_profile(self):
        profile = User.objects.create(username='me')
        self.assertEqual(str(profile), profile.username)
