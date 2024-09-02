from django.contrib import admin
from django.urls import path
# from .views import *
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('add/',views.add,name="add"),
    path('add/add_display',views.add_display,name="add_display"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('update/display_list/<int:id>/',views.display_list,name="display_list"),
    
]       
