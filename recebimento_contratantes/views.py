from django.shortcuts import render

def recebimento(request):
    return render(request,'recebimento_contratantes/recebimento.html')
