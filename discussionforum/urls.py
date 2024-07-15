from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [

    path('',views.home,name='home'),
    path('addInForum/',views.addInForum,name='addInForum'),
    path('addInDiscussion/',views.addInDiscussion,name='addInDiscussion'),
]