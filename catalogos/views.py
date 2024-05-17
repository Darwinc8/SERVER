from django.shortcuts import render
from .models import Emisor, Entidad, Dependencia, LOC, Edo_conservacion, Institucion, Tipo, Calibre, Marca, Modelo, Estatus_Arma, Tipo_Alta, Tipo_Dependencia, Tipo_Imagen, Municipio, TipoFuncinamiento, Propiedad
from django.contrib.auth.decorators import login_required
from .forms import BusquedaMunicipiosForm, BusquedaLOCsForm, BusquedaInstitucionesForm, BusquedaTiposForm, BusquedaCalibreForm, BusquedaMarcasForm, BusquedaModelosForm
from utilidades import utils
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
        return utils.BusquedaPersonalizada(request, query, valor, municipios, 'catalogos/municipios.html', BusquedaMunicipiosForm)
    
    return utils.CrearPaginador(request, municipios, 7, 'catalogos/municipios.html', BusquedaMunicipiosForm)

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
        return utils.BusquedaPersonalizada(request, query, valor, locs, 'catalogos/locs.html',BusquedaLOCsForm)
    
    return utils.CrearPaginador(request, locs, 12, 'catalogos/locs.html', BusquedaLOCsForm)

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
        return utils.BusquedaPersonalizada(request, query, valor, instituciones, 'catalogos/instituciones.html', BusquedaInstitucionesForm)
    
    return utils.CrearPaginador(request, instituciones, 7, 'catalogos/instituciones.html', BusquedaInstitucionesForm)

@login_required    
def tipos(request):
    tipos = Tipo.objects.all().order_by('ID_TIPO')
    
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    
    if query and valor:
        return utils.BusquedaPersonalizada(request, query, valor, tipos, 'catalogos/tipos.html', BusquedaTiposForm)
    
    return utils.CrearPaginador(request, tipos, 12, 'catalogos/tipos.html', BusquedaTiposForm)

@login_required
def calibres(request):
   calibres = Calibre.objects.all().order_by('ID_CALIBRE')
   query = request.GET.get('query')
   valor = request.GET.get('campos_filtrados')
   
   if query and valor:
       return utils.BusquedaPersonalizada(request, query, valor,calibres, 'catalogos/calibres.html', BusquedaCalibreForm)
   
   return utils.CrearPaginador(request, calibres, 12, 'catalogos/calibres.html', BusquedaCalibreForm)
    
@login_required
def marcas(request):
    marcas = Marca.objects.all().order_by('ID_MARCA')
    
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    
    if query and valor:
        return utils.BusquedaPersonalizada(request, query, valor, marcas, 'catalogos/marcas.html', BusquedaMarcasForm)
    
    return utils.CrearPaginador(request, marcas, 12, 'catalogos/marcas.html', BusquedaMarcasForm)

@login_required    
def modelos(request):
    modelos = Modelo.objects.all().order_by('ID_MODELO')
   
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')

    if query and valor:
        return utils.BusquedaPersonalizada(request, query, valor, modelos, 'catalogos/modelos.html', BusquedaModelosForm)
    
    return utils.CrearPaginador(request, modelos, 12, 'catalogos/modelos.html', BusquedaModelosForm)
 
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

@login_required    
def tipo_funcionamiento(request):
    tipos_funcionamientos = TipoFuncinamiento.objects.all()
    return render(request, 'catalogos/tipo_funcionamiento.html', {
        'tipos_funcionamientos':tipos_funcionamientos
    })

@login_required    
def propiedad(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'catalogos/propiedad.html', {
        'propiedades':propiedades
    })    
