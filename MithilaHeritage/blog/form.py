from django import forms
from django.db.models import fields
from froala_editor.widgets import FroalaEditor
from .models import *
class BlogForm(forms.ModelForm):
    class Meta:
        model=BlogModel
        fields=['content']
  #content = forms.CharField(widget=FroalaEditor)