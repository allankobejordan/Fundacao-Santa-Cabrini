from django.urls import path
from . import views

urlpatterns = [
    path('apenado/', views.apenado, name='apenado'),
]

