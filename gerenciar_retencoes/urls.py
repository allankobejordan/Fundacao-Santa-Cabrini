from django.urls import path
from . import views

urlpatterns = [
    path('gerenciar_retencoes/',views.gerenciar_retencoes,name="gerenciar_retencoes")
]
