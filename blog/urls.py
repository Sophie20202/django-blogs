
from django.urls import path
from .views import create_post, blog_list

urlpatterns = [
    path('', blog_list, name = "blog-list"),
    path('create/', create_post, name="create-blog"),
]
