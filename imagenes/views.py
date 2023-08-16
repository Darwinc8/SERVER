from django.shortcuts import render, redirect
from .models import Imagenes
from django.contrib.auth.decorators import login_required
from .forms import ImagenForm
from catalogos.models import Institucion
from django.http import JsonResponse
from armamento.forms import BusquedaForm
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
@login_required
def imagenes(request):
    imagenes = Imagenes.objects.all().order_by('ID_ARMA')
    query = request.GET.get('query')
    if query:
        imagenes = imagenes.filter(ID_ARMA__ID_ARMA__icontains=query)
    paginator = Paginator(imagenes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'imagenes.html', {
        'imagenes': page_obj,
        'form': BusquedaForm()
    })

@login_required
def crear_imagen(request):
    if request.method == 'GET':
        form = ImagenForm(request.POST)
        return render(request, 'crear_imagen.html', {
            'form': form
        })
    else:
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('imagenes')
        else:
            form = ImagenForm(request.POST)
        return render(request, 'crear_imagen.html', {
            'form': form
        })

@login_required
def eliminar_imagen(id):
    imagen = Imagenes.objects.get(ID_ALTERNA=id)
    imagen.delete()
    return redirect('imagenes')

@login_required
def editar_imagen(request, id):
        imagen = Imagenes.objects.get(ID_ALTERNA=id)
        form = ImagenForm(request.POST or None, request.FILES or None, instance=imagen)

        if form.is_valid() and request.POST:
            form.save()
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
    
    