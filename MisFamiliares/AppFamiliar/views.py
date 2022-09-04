from django.shortcuts import render
from .models import familia
from django.http import HttpResponse

# Create your views here.
def familia(request):
    cristina=familia(nombre="cristina", apellido="paz", edad=49, fecha=2022-edad)
    rodrigo=familia(nombre="rodrigo", apellido="zavalia", edad=51, fecha=2022-edad)
    belen=familia(nombre="belen", apellido="zavalia", edad=20, fecha=2022-edad)
    cristina.save()
    rodrigo.save()
    belen.save()

    familiar1=f"nombre {cristina.nombre} apellido {cristina.apellido} edad {cristina.edad} fecha {cristina.fecha}"
    familiar2=f"nombre {rodrigo.nombre} apellido {rodrigo.apellido} edad {rodrigo.edad} fecha {rodrigo.fecha}"
    familiar3=f"nombre {belen.nombre} apellido {belen.apellido} edad {belen.edad} fecha {belen.fecha}"

    return HttpResponse(familiar1,familiar2,familiar3)

def plantilla(request):
    archivo=open("C:\Users\salus\OneDrive\Escritorio\MVTSZavalia\MisFamiliares\Plantillas\template1.html")
    contenido=archivo.read()
    archivo.close()
    plantilla=template(contenido)
    contexto=context()
    documento=plantilla.render(contexto)

    return HttpResponse (documento)   
