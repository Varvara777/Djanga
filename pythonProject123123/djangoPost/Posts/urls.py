from django.contrib import admin
from django.urls import path,include
from. import views


urlpatterns = [
    path('', views.home, name='home'),
    path('post/create', views.create_post, name='post-create'),
    path('about/', views.about, name='about'),
]