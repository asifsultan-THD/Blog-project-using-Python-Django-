from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (index, PostDetailView, 
PostCreateView, PostUpdateView, 
PostDeleteView, aboutus, traveltips, famdes,
exploreindia, exploregermany, exploreegypt,
explorecolombia, explorenewyork, exploreparis,
add_comment_to_post, comment_approve, comment_remove)



class TestUrls(SimpleTestCase):

    def test_list_path_resolved(self):
        path = reverse('home')
        self.assertEquals(resolve(path).func, index)
        
    def test_detail_path_resolved(self):
        path = reverse('post-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.view_class, PostDetailView)

    def test_create_path_resolved(self):
        path = reverse('post-create')
        self.assertEquals(resolve(path).func.view_class, PostCreateView)
   
    def test_delete_path_resolved(self):
        path = reverse('post-delete', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.view_class, PostDeleteView)

    def test_update_path_resolved(self):
        path = reverse('post-update', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func.view_class, PostUpdateView)

    def test_add_comment_to_post_path_resolved(self):
        path = reverse('add_comment_to_post', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func, add_comment_to_post)

    def test_comment_approve_path_resolved(self):
        path = reverse('comment_approve', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func, comment_approve)

    def test_comment_remove_path_resolved(self):
        path = reverse('comment_remove', kwargs={'pk': 1})
        self.assertEquals(resolve(path).func, comment_remove)

    def test_aboutus_path_resolved(self):
        path = reverse('aboutus')
        self.assertEquals(resolve(path).func, aboutus)

    def test_traveltips_path_resolved(self):
        path = reverse('traveltips')
        self.assertEquals(resolve(path).func, traveltips)

    def test_famdes_path_resolved(self):
        path = reverse('famdes')
        self.assertEquals(resolve(path).func, famdes)

    def test_exploreindia_path_resolved(self):
        path = reverse('exploreindia')
        self.assertEquals(resolve(path).func, exploreindia)

    def test_exploregermany_path_resolved(self):
        path = reverse('exploregermany')
        self.assertEquals(resolve(path).func, exploregermany)

    def test_exploreegypt_path_resolved(self):
        path = reverse('exploreegypt')
        self.assertEquals(resolve(path).func, exploreegypt)

    def test_explorecolombia_path_resolved(self):
        path = reverse('explorecolombia')
        self.assertEquals(resolve(path).func, explorecolombia)

    def test_explorenewyork_path_resolved(self):
        path = reverse('explorenewyork')
        self.assertEquals(resolve(path).func, explorenewyork)

    def test_exploreparis_path_resolved(self):
        path = reverse('exploreparis')
        self.assertEquals(resolve(path).func, exploreparis)

       

   