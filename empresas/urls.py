from django.urls import path
from . import views

urlpatterns =[
    path('empresas/', views.empresas, name='empresas'),
]