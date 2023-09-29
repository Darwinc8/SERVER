from django.shortcuts import render
from django.core.paginator import Paginator
import os

from rnae.settings import IMAGES_ROOT 

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

def EliminarImagenAntigua(ruta):
    if os.path.isfile(ruta):
        os.remove(ruta)
        print(f"El archivo {ruta} ha sido eliminado con éxito.")
    else:
        print(f"El archivo {ruta} no existe.")
        
