from django.shortcuts import render
from django.core.paginator import Paginator
import os

def BusquedaPersonalizada(request, query, valor, lista, pagina, formulario):
    # Filtrar la lista
    lista_filtrada = lista.filter(**{valor: query})

    # Verificar si la lista filtrada está vacía
    if not lista_filtrada.exists():
        mensaje = f"No se encontraron registros con esos parametros."
        return render(request, pagina, {'mensaje': mensaje, 'form': formulario({'campos_filtrados': valor, 'query': query})})

    # Si hay registros, renderizar la lista
    return render(request, pagina, {'lista': lista_filtrada, 'form': formulario({'campos_filtrados': valor, 'query': query})})


def CrearPaginador(request, lista, num_paginas, pagina, formulario):
    paginator = Paginator(lista, num_paginas)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, pagina, {
        'lista': page_obj,
        'form': formulario()
    })

def EliminarImagenAntigua(ruta):
    # Verifica si el archivo existe
    if os.path.exists(ruta):
        # Si existe, elimínalo
        os.remove(ruta)
        print("Imagen antigua eliminada con exito")
    else:
        print("imagen no encontrada")    
        
