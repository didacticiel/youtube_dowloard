from django.contrib import admin 
from django.urls import path 
from ytapp import views

urlpatterns = [ 
	path('admin/', admin.site.urls), 
	path('youtube', views.youtube, name='youtube'), 
]