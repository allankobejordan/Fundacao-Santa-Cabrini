from django.urls import path
from . import views

urlpatterns = [
    path('beneficiarios/', views.beneficiarios, name='beneficiarios')
]
