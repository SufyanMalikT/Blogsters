from django.urls import path
from .views import *

urlpatterns = [
    path('',blog_home,name='blog_home'),
    path('about/', blog_about,name='blog_about'),
    path('category/',blog_cat,name='blog_cat'),
    path('<slug:slug>/', blog_details,name='blog_details'),
]