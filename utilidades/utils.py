from django.conf import settings
from django.shortcuts import render
from django.core.paginator import Paginator
import os 

def BusquedaPersonalizada(request, query, valor, lista, pagina, formulario):
    lista = lista.filter(**{valor: query})
    return render(request, pagina, {
    'lista': lista,
    'form': formulario({'campos_filtrados':valor, 'query':query})
    })

def CrearPaginador(request, lista, num_paginas, pagina, formulario):
    paginator = Paginator(lista, num_paginas)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, pagina, {
        'lista': page_obj,
        'form': formulario()
    })

def EliminarImagenAntigua(registro):
    imagen_path = os.path.join(registro.IMAGEN.path)
    print(imagen_path)
    if os.path.isfile(imagen_path):
        os.remove(imagen_path)