from django.urls import path 
from . import views

urlpatterns =[
    path('inicio/', views.index),
    path('fun1/', views.fun1),
]
