from django.shortcuts import render

def ordem_pagamento(request):
    return  render(request,'ordem_pagamento/ordem_pagamento.html')
