from django.conf import settings
from django.shortcuts import render
from django.core.paginator import Paginator
import os

from rnae.settings import PORTADORES_ROOT 

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
    # Ejemplo de uso
    imagen_path = os.path.join(PORTADORES_ROOT, registro.IMAGEN.name)

    if os.path.isfile(imagen_path):
        os.remove(imagen_path)
        print(f"El archivo {imagen_path} ha sido eliminado con éxito.")
    else:
        print(f"El archivo {imagen_path} no existe.")
