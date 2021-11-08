from django.urls import path
from . import views

urlpatterns = [
    path('dias_remidos/', views.dias_remidos, name='dias_remidos')
]
