from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>/', group_posts, name='group_list'),
    path('profile/<str:username>/', profile, name='profile'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/create/', post_create, name='create')
]