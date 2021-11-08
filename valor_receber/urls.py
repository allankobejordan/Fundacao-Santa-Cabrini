from django.urls import path
from  . import views

urlpatterns = [
    path('valor_receber/', views.valor_receber, name='valorReceber')
]