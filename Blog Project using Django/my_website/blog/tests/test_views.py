from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from blog.views import add_comment_to_post
from mixer.backend.django import mixer
from blog.models import Post, Comment
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('home')
        self.search_url = reverse('search')
        self.aboutus_url = reverse('aboutus')
        self.traveltips_url = reverse('traveltips')
        self.famdes_url = reverse('famdes')
        
      



    def test_project_search_GET(self):
            response = self.client.get(self.search_url)

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'search_results.html')

    def test_project_list_GET(self):
            response = self.client.get(self.list_url)

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'blog/index.html')


    def test_project_aboutus_GET(self):
            response = self.client.get(self.aboutus_url)

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'blog/aboutus.html')

    def test_project_traveltips_GET(self):
            response = self.client.get(self.traveltips_url)

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'blog/traveltips.html')

    def test_project_famdes_GET(self):
            response = self.client.get(self.famdes_url)

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'blog/famdes.html')

    def test_project_add_comment_authenticated(self):
        mixer.blend('blog.Post')
        path = reverse('post-detail', kwargs={'pk':1})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = add_comment_to_post(request, pk=1)
        assert response.status_code == 200

   




    

    





    


            


