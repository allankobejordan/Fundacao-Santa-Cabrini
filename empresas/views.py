from django.shortcuts import render

def empresas(request):
    return render(request,'empresas/empresa.html')
