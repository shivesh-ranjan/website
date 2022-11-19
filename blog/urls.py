from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blogHome"),
    path('blogPost/<str:slug>', views.blogPost, name="blogPost"),
    path('search', views.searchBlog, name="searchBlog")
]
