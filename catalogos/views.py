from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Emisor, Entidad, Dependencia, LOC, Edo_conservacion, Institucion, Tipo, Calibre, Marca, Modelo, Estatus_Arma, Tipo_Alta, Tipo_Dependencia, Tipo_Imagen, Municipio
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    usuario = request.user.username
    return render(request,'index.html', {
        'usuario':usuario
    })

@login_required
def catalogos(request):
    return render(request,'catalogos.html')

@login_required
def emisores(request):
    emisores = Emisor.objects.all()
    return render(request, 'catalogos/emisores.html',{
        'emisores': emisores
    })

@login_required
def entidades(request):
    entidades = Entidad.objects.all()
    return render(request, 'catalogos/entidades.html', {
        'entidades': entidades
    })
 
@login_required   
def municipios(request):
    municipios = Municipio.objects.order_by('ID_ENTIDAD', 'ID_MUNICIPIO')
    query = request.GET.get('query')
    if query:
        municipios = municipios.filter(MUNICIPIO__icontains=query)
    paginator = Paginator(municipios, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogos/municipios.html', {
        'municipios': page_obj,
        'form': BusquedaForm()
    })

@login_required
def dependencias(request):
    dependencias = Dependencia.objects.all()
    return render(request, 'catalogos/dependencias.html', {
        'dependencias':dependencias
    })

@login_required    
def locs(request):
    locs = LOC.objects.all().order_by('NO_LICENCIA')
    query = request.GET.get('query')
    if query:
        locs = locs.filter(NO_LICENCIA__icontains=query)
    paginator = Paginator(locs, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogos/locs.html', {
        'locs': page_obj,
        'form': BusquedaForm()
    })

@login_required
def edo_conservacion(request):
    estados = Edo_conservacion.objects.all()
    return render(request, 'catalogos/edo_conservacion.html', {
        'estados': estados
    })

@login_required
def instituciones(request):
    instituciones = Institucion.objects.all().order_by('ID_INSTITUCION')
    query = request.GET.get('query')
    if query:
        instituciones = instituciones.filter(NOMBRE__icontains=query)
    paginator = Paginator(instituciones, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogos/instituciones.html', {
        'instituciones': page_obj,
        'form': BusquedaForm()
    })

@login_required    
def tipos(request):
    tipos = Tipo.objects.all()
    query = request.GET.get('query')
    if query:
        tipos = tipos.filter(TIPO__icontains=query)
    paginator = Paginator(tipos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogos/tipos.html', {
        'tipos': page_obj,
        'form': BusquedaForm()
    })

@login_required
def calibres(request):
    calibres = Calibre.objects.all().order_by('ID_CALIBRE')
    query = request.GET.get('query')
    if query:
        calibres = calibres.filter(CALIBRE__icontains=query)
    paginator = Paginator(calibres, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogos/calibres.html', {
        'calibres': page_obj,
        'form': BusquedaForm()
    })

@login_required
def marcas(request):
    marcas = Marca.objects.all()
    query = request.GET.get('query')
    if query:
        marcas = marcas.filter(MARCA__icontains=query)
    paginator = Paginator(marcas, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogos/marcas.html', {
        'marcas': page_obj,
        'form': BusquedaForm()
    })

@login_required    
def modelos(request):
    modelos = Modelo.objects.all()
    paginator = Paginator(modelos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogos/modelos.html', {
        'modelos': page_obj
    })

@login_required
def estatus_arma(request):
    estatus = Estatus_Arma.objects.all()
    return render(request, 'catalogos/estatus_arma.html', {
        'estatus': estatus
    })

@login_required    
def tipo_alta(request):
    tipos = Tipo_Alta.objects.all()
    return render(request, 'catalogos/tipos_alta.html', {
        'tipos': tipos
    })

@login_required
def tipo_dependencia(request):
    tipos = Tipo_Dependencia.objects.all()
    return render(request, 'catalogos/tipos_dependencia.html', {
        'tipos': tipos
    })

@login_required    
def tipo_imagen(request):
    tipos = Tipo_Imagen.objects.all()
    return render(request, 'catalogos/tipos_imagen.html', {
        'tipos':tipos
    })
