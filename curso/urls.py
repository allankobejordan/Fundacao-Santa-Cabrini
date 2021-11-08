from django.urls import path
from . import views 

urlpatterns = [
    path('curso/', views.curso, name='curso'),
]