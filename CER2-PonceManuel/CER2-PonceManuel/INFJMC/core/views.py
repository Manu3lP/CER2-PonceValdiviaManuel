from django.shortcuts import render
from django.http import HttpResponse
from core.models import correos_M,Recidencia
menu = "<hr><ul>"
menu +=   " <li><a href=''>Inicio</a>"
menu +=   " <li><a href='correo/'>correo1</a>"
menu +=   " <li><a href='recidencia/'>recidencia</a>"
menu += "</ul>"


def home(request):
    return render(request,'core/index.html')

def correo(request):
    correspondencia=correos_M.objects.all()
    return render(request,'core/correo.html',{"correspondencia":correspondencia})

def recidencia(request):
    recidencia1=Recidencia.objects.all()
    return render(request,'core/recidencia.html',{"recidencia1":recidencia1})
