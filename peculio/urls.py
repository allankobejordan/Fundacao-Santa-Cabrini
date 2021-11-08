from django.urls import path
from . import views

urlpatterns = [
    path('peculio/', views.peculio, name='peculio')
]
