from django.shortcuts import render, redirect, get_object_or_404 
from .models import Portador
from .forms import PortadorForm, BusquedaPortadoresForm
from django.contrib.auth.decorators import login_required
import os
from django.contrib import messages
from utilidades import utils
# Create your views here.
@login_required
def portadores(request):
    portador = Portador.objects.all().order_by('NOMBRE')
    
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    
    if query and valor:
        return utils.BusquedaPersonalizada(request, query, valor, portador, 'portadores.html', BusquedaPortadoresForm)
        
    return utils.CrearPaginador(request, portador, 5, 'portadores.html', BusquedaPortadoresForm) 

@login_required 
def crear_portador(request):
    if request.method == 'GET':
        form = PortadorForm(request.POST or None, initial={'usuario': request.user})
        return render(request, 'create_portador.html', {
            'form': form
        })
    else:
        form = PortadorForm(request.POST, request.FILES, initial={'usuario': request.user})
        if form.is_valid():
            form.save()
            return redirect('portadores')
        else:
            messages.error(request, 'Error al crear portador, verifique los datos')
            return redirect('crear_portador')
 
@login_required
def editar_portador(request, id):
    portador =  get_object_or_404(Portador,pk=id)
    ruta = portador.IMAGEN.path
    form = PortadorForm(request.POST or None, request.FILES or None, instance=portador)
    if form.is_valid() and request.method == 'POST':
        if request.FILES:
            utils.EliminarImagenAntigua(ruta)
        form.save()
        return redirect('portadores')
    return render(request, 'editar_portador.html', {
    'form': form
    })

@login_required
def eliminar_portador(request, id):
    try:
        # Obtiene el registro por su ID, si no existe, lanzará una excepción 404
        registro = get_object_or_404(Portador, pk=id)

        # Obtiene la ruta completa de la imagen
        imagen_path = os.path.join(registro.IMAGEN.path)
        
        #Actualiza el campo usuario de quien lo elimino
        registro.usuario = request.user
        registro.save()
        # Borra el registro y luego la imagen
        registro.delete()
        os.remove(imagen_path)
        
    except Exception as e:
        # Si ocurre una excepción, maneja el error apropiadamente
        messages.error(request, f'Error al eliminar: {e}')
        
    return redirect('portadores')  # Redirige a la misma vista

          