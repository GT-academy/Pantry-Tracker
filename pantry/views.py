from django.shortcuts import render, redirect
from .models import Item
from datetime import date, timedelta

def lista_articulos(request):
    hoy = date.today()
    articulos = Item.objects.filter(usado=False)
    articulos_por_caducar = articulos.filter(fecha_caducidad__lte=hoy + timedelta(days=3))
    return render(request, 'pantry/lista_articulos.html', {
        'articulos': articulos,
        'articulos_por_caducar': articulos_por_caducar,
    })

def agregar_articulo(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        cantidad = int(request.POST['cantidad'])
        fecha_caducidad = request.POST['fecha_caducidad']
        Item.objects.create(nombre=nombre, cantidad=cantidad, fecha_caducidad=fecha_caducidad)
        return redirect('/')
    return render(request, 'pantry/agregar_articulo.html')

def marcar_usado(request, id):
    articulo = Item.objects.get(id=id)
    articulo.usado = True
    articulo.save()
    return redirect('/')

def eliminar_articulo(request, id):
    articulo = Item.objects.get(id=id)
    articulo.delete()
    return redirect('/')

from django.shortcuts import get_object_or_404

def editar_articulo(request, id):
    articulo = get_object_or_404(Item, id=id)
    if request.method == "POST":
        articulo.nombre = request.POST['nombre']
        articulo.cantidad = int(request.POST['cantidad'])
        articulo.fecha_caducidad = request.POST['fecha_caducidad']
        articulo.save()
        return redirect('/')
    return render(request, 'pantry/editar_articulo.html', {'articulo': articulo})

def lista_articulos(request):
    query = request.GET.get('q', '')
    hoy = date.today()
    articulos = Item.objects.filter(usado=False)
    if query:
        articulos = articulos.filter(nombre__icontains=query)
    articulos_por_caducar = articulos.filter(fecha_caducidad__lte=hoy + timedelta(days=3))
    return render(request, 'pantry/lista_articulos.html', {
        'articulos': articulos,
        'articulos_por_caducar': articulos_por_caducar,
        'query': query,
    })

import csv
from django.http import HttpResponse

def exportar_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="articulos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Cantidad', 'Fecha de Caducidad', 'Usado'])

    articulos = Item.objects.all()
    for articulo in articulos:
        writer.writerow([articulo.nombre, articulo.cantidad, articulo.fecha_caducidad, articulo.usado])

    return response

def historial_usados(request):
    usados = Item.objects.filter(usado=True)
    return render(request, 'pantry/historial_usados.html', {'usados': usados})