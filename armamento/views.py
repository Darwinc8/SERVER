import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Armamento
from .forms import ArmamentoForm, BusquedaArmamentoForm
from django.contrib.auth.decorators import login_required
from .models import Municipio, Institucion
from django.contrib import messages
from utilidades import utils
from django.utils.formats import localize

# Create your views here.
@login_required
def armamento(request):
    armamentos = Armamento.objects.all().order_by('ID_ALTERNA')
    
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    
    if query and valor:
        return utils.BusquedaPersonalizada(request, query, valor, armamentos, 'armamento.html', BusquedaArmamentoForm)
        
    return utils.CrearPaginador(request, armamentos, 5, 'armamento.html', BusquedaArmamentoForm)

@login_required
def crear_armamento(request):
    form = ArmamentoForm(request.POST or None,initial={'usuario': request.user})
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('armamento')
    else:
        return render(request, 'crear_armamento.html', {
        'form': form
        })

@login_required
def editar_armamento(request, id):
    objeto = get_object_or_404(Armamento, pk=id)
    form = ArmamentoForm(request.POST or None, initial={'usuario': request.user}, instance=objeto)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('armamento')
    else:
        objeto = convertir_fechas(objeto)
        form = ArmamentoForm(instance=objeto, initial={'usuario': request.user})

    return render(request, 'editar_armamento.html', {'form': form})

@login_required
def eliminar_armamento(request, id):
    try:
        #Obten el registro por su ID, si no existe, lanzará una excepción 404
        registro = get_object_or_404(Armamento, pk=id)
        
        #Actualiza el campo usuario de quien lo elimino
        registro.usuario = request.user
        registro.save()
        
        # Borra el registro
        registro.delete()
        
    except Exception as e:
        # Si ocurre una excepción, maneja el error apropiadamente
        messages.error(request, f'Error al eliminar: {e}')
        
    return redirect('armamento')  # Redirige a la misma vista  

def convertir_fechas(objeto):
    if objeto.FECHA: objeto.FECHA = objeto.FECHA.strftime("%Y-%m-%d")
    if objeto.FECHA_LOC: objeto.FECHA_LOC = objeto.FECHA_LOC.strftime("%Y-%m-%d")
    if objeto.FECHA_CAPTURA: objeto.FECHA_CAPTURA = objeto.FECHA_CAPTURA.strftime("%Y-%m-%d")
    if objeto.FECHA_BAJA_LOGICA: objeto.FECHA_BAJA_LOGICA= objeto.FECHA_BAJA_LOGICA.strftime("%Y-%m-%d")
    if objeto.FECHA_BAJA_DOCUMENTO: objeto.FECHA_BAJA_DOCUMENTO = objeto.FECHA_BAJA_DOCUMENTO.strftime("%Y-%m-%d")
    return objeto

def obtener_municipios(request, entidad_id):
    try:
        municipios = Municipio.objects.filter(ID_ENTIDAD__ID_ENTIDAD=entidad_id).values('id', 'MUNICIPIO')

        return JsonResponse(list(municipios), safe=False)

    except Municipio.DoesNotExist:
        # Manejo de error si no se encuentra la entidad o no existen municipios asociados
        print("Municipio o entidad no encontrados.")
        return JsonResponse([], safe=False)

def obtener_instituciones(request, dependencia_id):
    try:
        instituciones = Institucion.objects.filter(ID_DEPENDENCIA=dependencia_id).values('ID_INSTITUCION', 'NOMBRE')

        return JsonResponse(list(instituciones), safe=False)

    except Institucion.DoesNotExist:
        # Manejo de error si no se encuentra o no existen instituciones asociadas
        print("Instituciones no encontradas.")
        return JsonResponse([], safe=False)   