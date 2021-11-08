from django.shortcuts import render

def salarios_pagos(request):
    return render(request,'salarios_pagos/salarios_pagos.html')
