from django.test import TestCase
from blog.models import Post, Comment

class TestModels(TestCase):

    def test_project_post(self):
        post = Post(title="post 1", content="This is post one ")
        self.assertEqual(str(post), post.title)


    def test_project_comment(self):
        comment = Comment(author="comment 1", text="This is comment one ")
        self.assertEqual(str(comment), comment.text)