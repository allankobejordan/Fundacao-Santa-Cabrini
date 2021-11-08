from django.shortcuts import render

def folha_pagamento(request):
    return render(request,'folha_pagamento/folha_pagamento.html')
