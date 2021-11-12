from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils.timezone import now
from django.utils.text import slugify
from .helpers import *
from froala_editor.fields import FroalaField
# Create your models here.

class BlogModel(models.Model):
    sno= models.AutoField(primary_key=True)
    title= models.CharField(max_length=1000)
    content= FroalaField()
    user=models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    slug= models.SlugField(max_length=1000,null=True,blank=True)
    image=models.ImageField(upload_to='blog/img')
    created_at=models.DateTimeField(blank=True,auto_now_add=True)
    upload_to=models.DateTimeField(blank=True,auto_now_add=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)


    
class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(BlogModel,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:13]+" ... by "+self.user.username


# class BlogComment(models.Model):
#     sno=models.AutoField(primary_key=True)
#     comment=models.TextField()
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     post=models.ForeignKey(Post,on_delete=models.CASCADE)
#     parent=models.ForeignKey('self',on_delete=CASCADE,null=True)
#     timestamp=models.DateTimeField(default=now)
#     def __str__(self):
#         return self.comment[0:13]+" ... by "+self.user.username


class Post(models.Model):
     sno= models.AutoField(primary_key=True)
     title= models.CharField(max_length=255)
     content= models.TextField()
     author= models.CharField(max_length=20)
     slug= models.CharField(max_length=140)
     timeStamp=models.DateTimeField(blank=True)

     def __str__(self):
         return self.title+' by '+ self.author