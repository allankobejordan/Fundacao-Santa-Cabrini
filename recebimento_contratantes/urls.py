from django.urls import path
from . import views

urlpatterns = [
    path('recebimento_contratantes/',views.recebimento, name='recebimento')
]
