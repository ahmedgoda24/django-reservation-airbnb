from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author' , on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blog/')
    category = models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)
    slug = models.SlugField(blank=True, null=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.title)    
       super(Post, self).save(*args, **kwargs) # Call the real save() method


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name