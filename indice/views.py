from django.shortcuts import render

def indice(request):
    return render(request, 'indice/indice.html')
