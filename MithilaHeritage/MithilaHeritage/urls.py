"""MithilaHeritage URL Configuration


"""
from os import startfile
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.site.site_header="Mithila Heritage Admin"
admin.site.site_title="Mithila Heritage Admin Panel"
admin.site.index_title="Welcome to Mithila Heritage admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MithilaStuff.urls')),
    path('blog/',include('blog.urls')),
    path('froala_editor/',include('froala_editor.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
