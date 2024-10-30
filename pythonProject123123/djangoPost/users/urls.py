from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path,include
from .views import RegisterView

#from Posts import views

urlpatterns = [
    path('login/',views.sign_in,name='login'),
    path('logout/',views.sign_out,name='logout'),
    path('register/',RegisterView,name='register'),

]