from django.shortcuts import render
from django.core.paginator import Paginator
import os
from django.utils.translation import gettext_lazy as _

def BusquedaPersonalizada(request, query, valor, lista, pagina, formulario):
    # Filtrar la lista
    lista_filtrada = lista.filter(**{valor: query})
    lista_filtrada = lista_filtrada[:50]
    # Verificar si la lista filtrada está vacía
    if not lista_filtrada.exists():
        mensaje = _("No se encontraron registros con esos parámetros.")
        return render(request, pagina, {'mensaje': mensaje, 'form': formulario({'campos_filtrados': valor, 'query': query})})

    return render(request, pagina, {
        'lista': lista_filtrada,
        'form': formulario({'campos_filtrados': valor, 'query': query})
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
    # Verifica si el archivo existe
    if os.path.exists(ruta):
        # Si existe, elimínalo
        os.remove(ruta)   
        
