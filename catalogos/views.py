from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Emisor, Entidad, Dependencia, LOC, Edo_conservacion, Institucion, Tipo, Calibre, Marca, Modelo, Estatus_Arma, Tipo_Alta, Tipo_Dependencia, Tipo_Imagen, Municipio
from django.contrib.auth.decorators import login_required
from .forms import BusquedaMunicipiosForm, BusquedaLOCsForm, BusquedaInstitucionesForm, BusquedaTiposForm, BusquedaCalibreForm, BusquedaMarcasForm
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
    valor = request.GET.get('campos_filtrados')
    if query and valor:
        municipios = municipios.filter(**{valor: query})
    paginator = Paginator(municipios, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogos/municipios.html', {
        'municipios': page_obj,
        'form': BusquedaMunicipiosForm()
    })

@login_required
def dependencias(request):
    dependencias = Dependencia.objects.all().order_by('DEPENDENCIA')
    return render(request, 'catalogos/dependencias.html', {
        'dependencias':dependencias
    })

@login_required    
def locs(request):
    locs = LOC.objects.all().order_by('NO_LICENCIA')
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    if query and valor:
        locs = locs.filter(**{valor: query})
    paginator = Paginator(locs, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogos/locs.html', {
        'locs': page_obj,
        'form': BusquedaLOCsForm()
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
    valor = request.GET.get('campos_filtrados')
    if query and valor:
        instituciones = instituciones.filter(**{valor: query})
    paginator = Paginator(instituciones, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogos/instituciones.html', {
        'instituciones': page_obj,
        'form': BusquedaInstitucionesForm()
    })

@login_required    
def tipos(request):
    tipos = Tipo.objects.all()
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    if query and valor:
        tipos = tipos.filter(**{valor: query})
    paginator = Paginator(tipos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogos/tipos.html', {
        'tipos': page_obj,
        'form': BusquedaTiposForm()
    })

@login_required
def calibres(request):
    calibres = Calibre.objects.all().order_by('ID_CALIBRE')
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    if query and valor:
        calibres = calibres.filter(**{valor: query})
    paginator = Paginator(calibres, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogos/calibres.html', {
        'calibres': page_obj,
        'form': BusquedaCalibreForm()
    })

@login_required
def marcas(request):
    marcas = Marca.objects.all()
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    if query and valor:
        marcas = marcas.filter(**{valor: query})
    paginator = Paginator(marcas, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalogos/marcas.html', {
        'marcas': page_obj,
        'form': BusquedaMarcasForm()
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
