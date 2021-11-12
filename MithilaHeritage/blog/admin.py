from django.contrib import admin
from blog.models import BlogComment,BlogModel
# Register your models here.
admin.site.register((BlogComment,BlogModel))       