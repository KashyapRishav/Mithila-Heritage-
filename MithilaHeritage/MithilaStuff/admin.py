from django.contrib import admin
from .models import Contact,Material,Categories

# Register your models here.
admin.site.register(Contact)
admin.site.register(Categories)
admin.site.register(Material)