from django.urls import path
from . import views
urlpatterns = [
    path("postComment", views.postComment,name="postComment"),
    path("addBlog", views.add_blog,name="addBlog"),
    path("seeBlog", views.seeBlog,name="seeBlog"),
    path("blogDelete/<sno>", views.blogDelete,name="blogDelete"),
    path("blogEdit/<slug>", views.blogEdit,name="blogEdit"),
    path("", views.blogHome,name="blogHome"),
    path("<str:slug>", views.blogPost,name="blogPost"),
    
     
]