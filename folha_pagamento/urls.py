from django.urls import path
from . import views

urlpatterns = [
    path('',views.folha_pagamento, name='folha_pagamento' )
]
