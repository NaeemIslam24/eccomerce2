from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Post(models.Model):
      catagory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
      headline = models.CharField(max_length=240)
      sub_headline = models.CharField(max_length=250 , blank=True, null=True)
      thumbnail = models.ImageField(blank=True,null=True,upload_to='images/')
      body = RichTextField()
      author = models.ForeignKey(User, blank=True,on_delete= models.CASCADE, related_name='blog_post')
      slug = models.SlugField(blank=True,null=True)
      active = models.BooleanField(default=False)
      published = models.DateTimeField(default=timezone.now)
      created = models.DateTimeField(auto_now_add=True)

 

      class Meta:
            ordering = ('-published',)


      def __str__(self):
            return self.headline