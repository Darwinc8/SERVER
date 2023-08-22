from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator 
from .models import Portador
from .forms import PortadorForm
from .forms import BusquedaPortadoresForm
from django.contrib.auth.decorators import login_required
import os
from django.contrib import messages

# Create your views here.
@login_required
def portadores(request):
    portador = Portador.objects.all().order_by('NOMBRE')
    
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    
    if query and valor:
        portador = portador.filter(**{valor: query})
        return render(request, 'portadores.html', {
        'portadores': portador,
        'form': BusquedaPortadoresForm({'campos_filtrados':valor,'query':query
        })
    })
    paginator = Paginator(portador, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'portadores.html', {
        'portadores': page_obj,
        'form': BusquedaPortadoresForm()
    }) 

@login_required    
def crear_portador(request):
    if request.method == 'GET':
        form = PortadorForm(request.POST or None)
        return render(request, 'create_portador.html', {
            'form': form
        })
    else:
        form = PortadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portadores')
        else:
            messages.error(request, 'Error al crear portador, verifique los datos')
            return redirect('crear_portador')
 
@login_required    
def editar_portador(request, id):
    portador =   get_object_or_404(Portador,CUIP=id)
    form = PortadorForm(request.POST or None, request.FILES or None, instance=portador)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('portadores')
    return render(request, 'edit_portador.html', {
    'form': form
    })

@login_required
def eliminar_portador(request, id):
    try:
        # Obtiene el registro por su ID, si no existe, lanzará una excepción 404
        registro = get_object_or_404(Portador, pk=id)

        # Obtiene la ruta completa de la imagen
        imagen_path = os.path.join(registro.IMAGEN.path)
        
        # Borra el registro y luego la imagen
        registro.delete()
        os.remove(imagen_path)
        
    except Exception as e:
        # Si ocurre una excepción, maneja el error apropiadamente
        messages.error(request, f'Error al eliminar: {e}')
        
    return redirect('portadores')  # Redirige a la misma vista
          