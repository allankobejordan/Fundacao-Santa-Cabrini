from django.urls import path
from . import views

urlpatterns = [
    path('salarios_pagos/',views.salarios_pagos, name='salarios_pagos')
]
