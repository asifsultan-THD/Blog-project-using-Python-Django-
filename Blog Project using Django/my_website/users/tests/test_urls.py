from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users import views as user_views
from django.contrib.auth import views as auth_views




class TestUrls(SimpleTestCase):

    def test_register_path_resolved(self):
        path = reverse('register')
        self.assertEquals(resolve(path).func, user_views.register)
        
    def test_profile_path_resolved(self):
        path = reverse('profile')
        self.assertEquals(resolve(path).func, user_views.profile)

    def test_login_path_resolved(self):
        path = reverse('login')
        self.assertEquals(resolve(path).func.view_class, auth_views.LoginView)
   
    def test_logout_path_resolved(self):
        path = reverse('logout')
        self.assertEquals(resolve(path).func.view_class, auth_views.LogoutView)

 



 

       

   