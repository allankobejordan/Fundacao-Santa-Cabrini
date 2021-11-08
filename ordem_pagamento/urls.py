from django.urls import path
from . import views

urlpatterns =[
    path('ordem_pagamento/', views.ordem_pagamento, name='ordem_pagamento')
]