from django.db import models
from froala_editor.fields import FroalaField
# Create your models here.
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
         return 'Message from '+ self.name


class Categories(models.Model):
    type= models.CharField(max_length=255,null=False,blank=False)
    desc= models.CharField(max_length=555,null=False,blank=False,default="")
    image=models.ImageField(upload_to='MithilaStuff/img' , default='MithilaStuff/img/image.jpeg')
    def __str__(self):
         return self.type



class Material(models.Model):
    name= models.CharField(max_length=255)
    type= models.ForeignKey(Categories,on_delete=models.CASCADE,related_name='types')
    content= FroalaField()
    image=models.ImageField(upload_to='MithilaStuff/img')

    def __str__(self):
         return self.name



     