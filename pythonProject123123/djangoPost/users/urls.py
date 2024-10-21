from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path,include

#from Posts import views

urlpatterns = [
    path('login/',views.sign_in,{'extend':'base.html'},name='login'),
    path('logout/',views.sign_out,name='logout'),

]