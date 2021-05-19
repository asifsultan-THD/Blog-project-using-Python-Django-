from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Tag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


#Post Section Program Part
class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now())
    image = models.FileField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    comment_count = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse('post-detail', kwargs={'pk': self.pk})


# Comment Section Program Part
class Comment(models.Model):
    post=models.ForeignKey('post', related_name='comments', on_delete = models.CASCADE)
    author=models.CharField(max_length=250)
    text=models.TextField(blank=True, null=True)
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()
#for the comments to be approved by superuser

    def get_absolute_url(self):
        return reverse('blog-home')
        #returning to the main page

    def __str__(self):
        return self.text
