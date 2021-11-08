from django.shortcuts import render

def beneficiarios(request):
    return render(request,'beneficiarios/beneficiarios.html')
