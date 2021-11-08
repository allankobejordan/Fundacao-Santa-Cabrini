from django.urls import path
from . import views

urlpatterns = [
    path('classificacoes/', views.classificacoes, name='classificacoes')
]
