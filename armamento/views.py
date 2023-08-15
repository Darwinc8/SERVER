from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Armamento
from django.core.paginator import Paginator
from .forms import ArmamentoForm, BusquedaForm
from django.contrib.auth.decorators import login_required
from .models import Municipio, Institucion

# Create your views here.
@login_required
def armamento(request):
    armamentos = Armamento.objects.all().order_by('ID_ALTERNA')
    query = request.GET.get('query')
    if query:
        armamentos = armamentos.filter(ID_ARMA__icontains=query)
    paginator = Paginator(armamentos, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'armamento.html', {
        'armamento': page_obj,
        'form': BusquedaForm()
    })

@login_required
def crear_armamento(request):
    if request.method == 'GET':
        form = ArmamentoForm(request.POST)
        return render(request, 'create_armamento.html', {
            'form': form
        })
    else:
        form = ArmamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('armamento')
        else:
            return render(request, 'create_armamento.html', {
            'form': form
        })

@login_required
def editar_armamento(request, id):
    objeto = get_object_or_404(Armamento, pk=id)
    
    if request.method == 'POST':
        form = ArmamentoForm(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            print("guardado")
            return redirect('armamento')
    else:
        objeto = convertir_fechas(objeto)
        form = ArmamentoForm(instance=objeto)

    return render(request, 'editar_armamento.html', {'form': form})

@login_required
def eliminar_armamento(request, id):
    armamento = Armamento.objects.get(ID_ALTERNA=id)
    armamento.delete()
    return redirect('armamento')  

def convertir_fechas(objeto):
    if objeto.FECHA: objeto.FECHA = objeto.FECHA.strftime("%Y-%m-%d")
    if objeto.FECHA_LOC: objeto.FECHA_LOC = objeto.FECHA_LOC.strftime("%Y-%m-%d")
    if objeto.FECHA_CAPTURA: objeto.FECHA_CAPTURA = objeto.FECHA_CAPTURA.strftime("%Y-%m-%d")
    if objeto.FECHA_BAJA_LOGICA: objeto.FECHA_BAJA_LOGICA= objeto.FECHA_BAJA_LOGICA.strftime("%Y-%m-%d")
    if objeto.FECHA_BAJA_DOCUMENTO: objeto.FECHA_BAJA_DOCUMENTO = objeto.FECHA_BAJA_DOCUMENTO.strftime("%Y-%m-%d")
    return objeto

def reconvertir_fechas(objeto):
    if objeto.FECHA: objeto.FECHA = objeto.FECHA.strftime("'%d de %B de %Y'")
    if objeto.FECHA_LOC: objeto.FECHA_LOC = objeto.FECHA_LOC.strftime("'%d de %B de %Y'")
    if objeto.FECHA_CAPTURA: objeto.FECHA_CAPTURA = objeto.FECHA_CAPTURA.strftime("'%d de %B de %Y'")
    if objeto.FECHA_BAJA_LOGICA: objeto.FECHA_BAJA_LOGICA = objeto.FECHA_BAJA_LOGICA.strftime("'%d de %B de %Y'")
    if objeto.FECHA_BAJA_DOCUMENTO: objeto.FECHA_BAJA_DOCUMENTO = objeto.FECHA_BAJA_DOCUMENTO.strftime("'%d de %B de %Y'")

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
