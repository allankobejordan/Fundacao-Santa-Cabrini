from django.urls import path
from . import views

urlpatterns = [
    path('gerar_remessas/',views.gerar_remessas, name='gerar_remessas')
]
