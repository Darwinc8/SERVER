import os
from django.shortcuts import get_object_or_404, render, redirect
from .models import Imagenes
from django.contrib.auth.decorators import login_required
from .forms import CrearImagenForm, EditarImagenForm
from catalogos.models import Institucion
from django.http import JsonResponse
from .forms import BusquedaImagenesForm
from django.contrib import messages
from utilidades import utils
# Create your views here.
@login_required
def imagenes(request):
    imagenes = Imagenes.objects.all().order_by('-ultima_modificacion')
    
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    
    if query and valor:
        return utils.BusquedaPersonalizada(request, query, valor, imagenes, 'imagenes.html', BusquedaImagenesForm)
        
    return utils.CrearPaginador(request, imagenes, 5, 'imagenes.html', BusquedaImagenesForm)

@login_required
def crear_imagen(request):
    if request.method == 'GET':
        form = CrearImagenForm(request.POST or None)
        return render(request, 'crear_imagen.html', {
            'form': form
        })
    else:
        form = CrearImagenForm(request.POST, request.FILES)
        if form.is_valid():
            objecto = form.save(commit=False)
            objecto.usuario = request.user
            objecto.save()
            return redirect('imagenes')
        else:
            print(form.errors)
            return redirect('crear_imagen')

@login_required
def eliminar_imagen(request, id):
    try:
        #Obten el registro por su ID, si no existe, lanzará una excepción 404
        registro = get_object_or_404(Imagenes, pk=id)
        
        # Obtén la ruta completa de la imagen
        imagen_path = os.path.join(registro.IMAGEN.path)
        
        #Actualiza el campo usuario de quien lo elimino
        Imagenes.objects.filter(pk=id).update(usuario=request.user)
        
        # Borra el registro y luego la imagen
        registro.delete()
        os.remove(imagen_path)
        
    except Exception as e:
        # Si ocurre una excepción, maneja el error apropiadamente
        messages.error(request, f'Error al eliminar: {e}')
        
    return redirect('imagenes')  # Redirige a la misma vista

@login_required
def editar_imagen(request, id):
        imagen = get_object_or_404(Imagenes,pk=id)
        ruta = f"/RNAE_V1{imagen.IMAGEN.url}"
        
        form = EditarImagenForm(request.POST or None, request.FILES or None, instance=imagen)

        if form.is_valid() and request.method == 'POST':
            if 'IMAGEN' in form.changed_data:
                utils.EliminarImagenAntigua(ruta)
            objeto = form.save(commit=False)
            objeto.usuario = request.user     
            objeto.save()    
            return redirect('imagenes')
        return render(request, 'editar_imagen.html', {
            'form': form
            })
        
@login_required
def obtener_instituciones(dependencia_id):
    try:
        instituciones = Institucion.objects.filter(ID_DEPENDENCIA=dependencia_id).values('ID_INSTITUCION', 'NOMBRE')

        return JsonResponse(list(instituciones), safe=False)

    except Institucion.DoesNotExist:
        # Manejo de error si no se encuentra o no existen instituciones asociadas
        print("Instituciones no encontradas.")
        return JsonResponse([], safe=False)
    
    