from django.test import SimpleTestCase
from blog.forms import CommentForm


class TestForms(SimpleTestCase):

    def test_comment_valid_data(self):
        form = CommentForm(data={
            'author':'me',
            'text':'I like your post so much'
        })

        self.assertTrue(form.is_valid())

    def test_comment_empty(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())


