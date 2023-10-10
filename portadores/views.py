from django.shortcuts import render, redirect, get_object_or_404 
from .models import Portador
from .forms import CrearPortadorForm, EditarPortadorForm, BusquedaPortadoresForm
from django.contrib.auth.decorators import login_required
import os
from django.contrib import messages
from utilidades import utils
# Create your views here.
@login_required
def portadores(request):
    portador = Portador.objects.all().order_by('-ultima_modificacion')
    
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    
    if query and valor:
        return utils.BusquedaPersonalizada(request, query, valor, portador, 'portadores.html', BusquedaPortadoresForm)
        
    return utils.CrearPaginador(request, portador, 5, 'portadores.html', BusquedaPortadoresForm) 

@login_required 
def crear_portador(request):
    if request.method == 'GET':
        form = CrearPortadorForm(request.POST or None)
        return render(request, 'create_portador.html', {
            'form': form
        })
    else:
        form = CrearPortadorForm(request.POST, request.FILES)
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.usuario = request.user
            objeto.save()
            return redirect('portadores')
        else:
            messages.error(request, 'Error al crear portador, verifique los datos')
            return redirect('crear_portador')
 
@login_required
def editar_portador(request, id):
    portador =  get_object_or_404(Portador,pk=id)
    ruta = f"/RNAE_V1{portador.IMAGEN.url}"

    form = EditarPortadorForm(request.POST or None, request.FILES or None, instance=portador)
    
    if form.is_valid() and request.method == 'POST':
        if 'IMAGEN' in form.changed_data:
            utils.EliminarImagenAntigua(ruta)
        objeto = form.save(commit=False)
        objeto.usuario = request.user     
        objeto.save()
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
        Portador.objects.filter(pk=id).update(usuario=request.user)
        # Borra el registro y luego la imagen
        registro.delete()
        os.remove(imagen_path)
        
    except:
        # Si ocurre una excepción, maneja el error apropiadamente
        messages.error(request, f'Error al eliminar: El portador está asignado como responsable/titular de un armamento.')
        
    return redirect('portadores')  # Redirige a la misma vista

          