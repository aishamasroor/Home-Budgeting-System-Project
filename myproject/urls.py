"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
RL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('load_form', views.load_form),
    path('add', views.add),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>/', views.delete),
    path('search', views.search),
    path('trans', views.transaction),
    path('transpage', views.transpage),
    path('save', views.save),
    path('showdetails', views.showdetails),
    path('submit', views.submit),
    path('show2', views.show2),
    path('categories', views.show_cat),
    path('deletes/<int:cat_id>/', views.deletes),

]
