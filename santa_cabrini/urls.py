"""santa_cabrini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('', include('home.urls')),
    path('cadastro/', include('empresas.urls')),
    path('cadastro/', include('apenado.urls')),
    path('cadastro/', include('curso.urls')),
    path('cadastro/', include('indice.urls')),
    path('cadastro/', include('salario.urls')),
    path('auditoria/', include('auditoria.urls')),
    path('folha_pagamento/', include('folha_pagamento.urls')),
    path('pagamento/', include('recebimento_contratantes.urls')),
    path('pagamento/', include('valor_receber.urls')),
    path('pagamento/', include('salarios_pagos.urls')),
    path('pagamento/', include('gerenciar_retencoes.urls')),
    path('pagamento/', include('gerar_remessas.urls')),
    path('pagamento/', include('peculio.urls')),
    path('pagamento/', include('ordem_pagamento.urls')),
    path('consulta/', include('beneficiarios.urls')),
    path('consulta/', include('classificacoes.urls')),
    path('consulta/', include('dias_remidos.urls')),
]
