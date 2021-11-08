from django.shortcuts import render

def salario(request):
    return render(request,'salario/salario.html')