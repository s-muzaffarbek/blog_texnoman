from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category_list'),
    path('', BlogView.as_view(), name='blog_list'),
    path('detail/<slug:slug>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<slug:slug>', CategoryBlogView.as_view(), name='blog_category'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('update/<slug:slug>', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<slug:slug>', BlogDeleteView.as_view(), name='blog_delete'),
    path('tag/<slug:slug>', TagView.as_view(), name='tag_filter'),
]