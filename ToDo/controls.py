from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
    path('home/', views.home, name='home'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
    path('mark_complete/<int:todo_id>', views.mark_complete, name="mark_complete"),
    path('mark_incomplete/<int:todo_id>', views.mark_incomplete, name="mark_incomplete"),
    path('edit/<int:todo_id>', views.edit, name="edit"),

]
'''
   path('master/', views.master, name='master'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('search/', views.search, name='search'),
   path('form/', views.details, name='details'),
   path('registration/', views.Registration, name='registration')
   '''
