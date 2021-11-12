from django.urls import path
from . import views 
urlpatterns = [
    path("", views.index,name="MithilaStuffHome"),
    path("contact", views.contact,name="contact"),
    path("search", views.search,name="search"),
    path("signup", views.handleSignup,name="handleSignup"),
    path("login", views.handleLogin,name="handleLogout"),
    path("logout", views.handleLogout,name="handleLogout"),
    path("seeMithilaStuff", views.seeMithilaStuff,name="seeMithilaStuff"),
]
