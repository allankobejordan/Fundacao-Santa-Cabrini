from django.shortcuts import render

def dias_remidos(request):
    return render(request, 'dias_remidos/dias_remidos.html')
