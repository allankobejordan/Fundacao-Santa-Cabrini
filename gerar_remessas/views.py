from django.shortcuts import render

def gerar_remessas(request):
    return render(request,'gerar_remessas/gerar_remessas.html')
