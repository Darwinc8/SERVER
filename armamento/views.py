from django.forms import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, FileResponse
from .models import Armamento, ArmamentoLog
from .forms import ArmamentoForm, BusquedaArmamentoForm, ExcelUploadForm, BajaArmamentoForm, ArmamentoLogForm
from django.contrib.auth.decorators import login_required
from .models import Municipio, Institucion, Dependencia, Entidad, LOC, Tipo, Calibre, Marca, Modelo, Edo_conservacion, Estatus_Arma, TipoFuncinamiento, Propiedad
from django.contrib import messages
from utilidades import utils
from django.db.models import Q
import pandas as pd
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your views here.
@login_required
def panel_armamento(request):
    return render(request, 'armamento_panel.html')

@login_required
def armamento(request):

    armamentos = Armamento.objects.all().order_by('-ultima_modificacion')
    
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    
    if query and valor:
        return utils.BusquedaPersonalizada(request, query, valor, armamentos, 'armamento.html', BusquedaArmamentoForm)
  
    return utils.CrearPaginador(request, armamentos, 5, 'armamento.html', BusquedaArmamentoForm)

@login_required
def armamento_activos(request):

    armamentos = Armamento.objects.filter(
    Q(FECHA_BAJA_LOGICA__isnull=True) &
    Q(MOTIVO_BAJA__isnull=True) | Q(MOTIVO_BAJA__exact='') &
    Q(DOCUMENTO_BAJA__isnull=True) | Q(DOCUMENTO_BAJA__exact='') &
    Q(OBSERVACIONES_BAJA__isnull=True) | Q(OBSERVACIONES_BAJA__exact='') &
    Q(FECHA_BAJA_DOCUMENTO__isnull=True)
).order_by('-ultima_modificacion')
    
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    
    if query and valor:
        return utils.BusquedaPersonalizada(request, query, valor, armamentos, 'activos_armamento.html', BusquedaArmamentoForm)
  
    return utils.CrearPaginador(request, armamentos, 5, 'activos_armamento.html', BusquedaArmamentoForm)

@login_required
def movimientos_armamento(request):
    movimientos = ArmamentoLog.objects.all().order_by('-ultima_modificacion')
    return utils.CrearPaginador(request, movimientos, 5, 'movimientos_armamento.html', ArmamentoLogForm)    

@login_required
def ver_movimiento(request, id):
    movimiento = get_object_or_404(ArmamentoLog, pk=id)
    form = ArmamentoLogForm(instance=movimiento)
        # Itera sobre los campos del formulario y establece el atributo "readonly" en True
    for field_name, field in form.fields.items():
        form.fields[field_name].disabled = True
    return render(request, 'formMovimientos.html', {'form': form,
                                                  'id': id})

@login_required
def armamento_inactivos(request):

    armamentos = Armamento.objects.exclude(
    Q(FECHA_BAJA_LOGICA__isnull=True) &
    Q(MOTIVO_BAJA__isnull=True) | Q(MOTIVO_BAJA__exact='') &
    Q(DOCUMENTO_BAJA__isnull=True) | Q(DOCUMENTO_BAJA__exact='') &
    Q(OBSERVACIONES_BAJA__isnull=True) | Q(OBSERVACIONES_BAJA__exact='') &
    Q(FECHA_BAJA_DOCUMENTO__isnull=True)
).order_by('-ultima_modificacion')
    
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    
    if query and valor:
        return utils.BusquedaPersonalizada(request, query, valor, armamentos, 'inactivos_armamento.html', BusquedaArmamentoForm)
  
    return utils.CrearPaginador(request, armamentos, 5, 'inactivos_armamento.html', BusquedaArmamentoForm)

@login_required
def crear_armamento(request):
    if request.method == 'POST':
        form = ArmamentoForm(request.POST)
        if form.is_valid():
            objecto = form.save(commit=False)
            objecto.usuario = request.user
            objecto.save()
            messages.success(request, 'El Armamento fue agregado exitosamente.')
            return redirect('armamento')
        else:
            return render(request, 'crear_armamento.html', {
                'form': form,
                'is_editing': False
            })
    else:
        form = ArmamentoForm()
        return render(request, 'crear_armamento.html', {
            'form': form,
            'is_editing': False
        })

@login_required
def crear_armamento_excel(request):
    if request.method == 'POST' and request.FILES['archivo_excel']:
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_excel = request.FILES['archivo_excel']
            
            # Procesar el archivo de Excel con pandas y openpyxl
            df = validar_plantilla_excel(request, archivo_excel)
            if df is None:
                return redirect('armamento_excel')   
            
             # Reemplazar NaN por 0 en columnas numéricas y celda vacia por ""
            df['Matricula_canon *'] = df['Matricula_canon *'].fillna("")
            df['Código de Identificación de Huella Balística (CIHB)'] = df['Código de Identificación de Huella Balística (CIHB)'].fillna("")
            df['Motivo de baja'] = df['Motivo de baja'].fillna("")
            df['Documento de baja'] = df['Documento de baja'].fillna("")
            df['Observaciones de baja'] = df['Observaciones de baja'].fillna("")
       
            
            for index, row in df.iterrows(): 
                try:
                   #Convertimos los ids de los campos al excel a objetos para manejarlos
                    fila_institucion = obtener_institucion_id(request, (row['Institución']))
                    fila_dependencia = obtener_dependencia_id(request, (row['Dependencia']))
                    fila_entidad = obtener_entidad_id(request, (row['Entidad']), )
                    fila_municipio = obtener_municipio_id(request, (row['Municipio']),fila_entidad.ID_ENTIDAD)
                    fila_loc = obtener_loc_id(request, (row['Número de licencia oficial colectiva']))
                    fila_ClaseTipoArma = obtener_claseTipoArma_id(request, (row['Clase/Tipo de arma']))
                    fila_calibre = obtener_calibre_id(request, (row['Calibre del arma']))
                    fila_marca = obtener_marca_id(request, (row['Marca del arma']))
                    fila_modelo = obtener_modelo_id(request, (row['Modelo del arma']))
                    fila_edoConservacion =  obtener_edoConservacion_id(request, (row['Estado del arma']))
                    fila_estatus = obtener_statusArma_id(request, (row['Estatus del arma']))
                    fila_tipoFuncionamiento = obtener_tipoFuncionamiento_id(request, (row['Tipo de Funcionamiento']))
                    fila_propiedad = obtener_propiedad_id(request, (row['Propiedad']))

                    fila_id_arma = transformar_numero(request,(row['ID Arma']), row, 'ID Arma')
                    fila_fecha_registro = transformar_fecha(request, (row['Fecha de registro']), 'Fecha de Registro', row)
                    fila_fecha_loc = transformar_fecha(request, (row['Fecha de alta en la LOC']), 'Fecha de alta en la LOC', row)
                    fila_fecha_captura = transformar_fecha(request, (row['Fecha de alta/captura']), 'Fecha de alta/captura', row)
                    fila_fecha_baja_logica = transformar_fecha(request, (row['Fecha de baja logica']), 'Fecha de baja logica', row)
                    fila_fecha_baja_documento = transformar_fecha(request, (row['Fecha de baja del documento']), 'Fecha de baja del documento', row)
                except ValidationError as ve:
                    # Capturar y mostrar el error en la plantilla
                    messages.error(request, ve.message)
                    return render(request, 'excel_armamento.html', {'form': form})
                 
                 # Verificar si la fila ya existe en la base de datos
                try:
                    objeto = Armamento.objects.get(MATRICULA=row['Matrícula'])
                    modificado=False 
                    # Verificar si existen diferencias en los campos y actualizar si es necesario
                    if objeto.ID_ARMA != fila_id_arma:
                        modificado = True
                        objeto.ID_ARMA = fila_id_arma

                    if objeto.INSTITUCION != fila_institucion:
                        modificado = True
                        objeto.INSTITUCION = fila_institucion
                        
                    if objeto.DEPENDENCIA != fila_dependencia:
                        modificado = True
                        objeto.DEPENDENCIA = fila_dependencia
                        
                    if objeto.ENTIDAD != fila_entidad:
                        modificado = True
                        objeto.ENTIDAD = fila_entidad
                    
                    if objeto.MUNICIPIO != fila_municipio:
                        modificado = True
                        objeto.MUNICIPIO = fila_municipio
                        
                    if objeto.NUMERO_LOC != fila_loc:
                        modificado = True
                        objeto.NUMERO_LOC = fila_loc
                    
                    if objeto.FOLIO_C != row['Folio C']:
                        modificado = True
                        objeto.FOLIO_C = row['Folio C']
                    
                    if objeto.FOLIO_D != row['Folio D']:
                        modificado = True
                        objeto.FOLIO_D = row['Folio D']
                        
                    if objeto.CLASE_TIPO_ARMA != fila_ClaseTipoArma:
                        modificado = True
                        objeto.CLASE_TIPO_ARMA = fila_ClaseTipoArma
                         
                    if objeto.CALIBRE_ARMA != fila_calibre:
                        modificado = True
                        objeto.CALIBRE_ARMA = fila_calibre
                    
                    if objeto.MARCA_ARMA != fila_marca:
                        modificado = True
                        objeto.MARCA_ARMA = fila_marca 
                     
                    if objeto.MODELO_ARMA != fila_modelo:
                        modificado = True
                        objeto.MODELO_ARMA = fila_modelo
                                        
                    if objeto.MATRICULA_CANON != row['Matricula_canon *']:
                        modificado = True
                        objeto.MATRICULA_CANON = row['Matricula_canon *']   
                                       
                    fecha_objeto_registro = pd.to_datetime(objeto.FECHA).strftime('%Y-%m-%d')
                    if fecha_objeto_registro != fila_fecha_registro:
                        modificado = True
                        objeto.FECHA = fila_fecha_registro 
                        
                    fecha_objeto_loc = pd.to_datetime(objeto.FECHA_LOC).strftime('%Y-%m-%d')
                    if fecha_objeto_loc != fila_fecha_loc:
                        modificado = True
                        objeto.FECHA_LOC = fila_fecha_loc
                    
                    if objeto.ESTADO_ARMA != fila_edoConservacion:
                        modificado = True
                        objeto.ESTADO_ARMA = fila_edoConservacion
                     
                    fecha_objeto_captura = pd.to_datetime(objeto.FECHA_CAPTURA).strftime('%Y-%m-%d')    
                    if fecha_objeto_captura != fila_fecha_captura:
                        modificado = True
                        objeto.FECHA_CAPTURA = fila_fecha_captura
                    
                    if objeto.OBSERVACIONES != row['Observaciones']:
                        modificado = True
                        objeto.OBSERVACIONES = row['Observaciones']
                    
                    if objeto.ESTATUS_ARMA != fila_estatus:
                        modificado = True
                        objeto.ESTATUS_ARMA = fila_estatus
                        
                    if objeto.CUIP_PORTADOR != row['CUIP del elemento que la porta']:
                        modificado = True
                        objeto.CUIP_PORTADOR = row['CUIP del elemento que la porta']
                    
                    if objeto.CUIP_RESPONSABLE != row['CUIP del elemento responsable del cargo']:
                        modificado = True
                        objeto.CUIP_RESPONSABLE = row['CUIP del elemento responsable del cargo']
                    
                    if objeto.CIHB != row['Código de Identificación de Huella Balística (CIHB)']:
                        modificado = True
                        objeto.CIHB = row['Código de Identificación de Huella Balística (CIHB)']
                        
                    if objeto.TIPO_FUNCIONAMIENTO != fila_tipoFuncionamiento:
                        modificado = True
                        objeto.TIPO_FUNCIONAMIENTO = fila_tipoFuncionamiento
                    
                    if objeto.PROPIEDAD != fila_propiedad:
                        modificado = True
                        objeto.PROPIEDAD = fila_propiedad
                    

                    if pd.notna(row['Fecha de baja logica']):
                        if objeto.FECHA_BAJA_LOGICA is not None:
                            fecha_objeto_baja_logica = pd.to_datetime(objeto.FECHA_BAJA_LOGICA).strftime('%Y-%m-%d')
                            fecha_baja_logica = transformar_fecha(request, (row['Fecha de baja logica']), 'Fecha de baja logica', row)
                            if fecha_objeto_baja_logica != fecha_baja_logica:
                                modificado = True
                                objeto.FECHA_BAJA_LOGICA = row['Fecha de baja logica']
                        else:
                            modificado = True
                            objeto.FECHA_BAJA_LOGICA = row['Fecha de baja logica']


                    if objeto.MOTIVO_BAJA != row['Motivo de baja']:
                        modificado = True
                        print(modificado)
                        objeto.MOTIVO_BAJA = row['Motivo de baja']

                    if objeto.DOCUMENTO_BAJA != row['Documento de baja']:
                        modificado = True
                        objeto.DOCUMENTO_BAJA = row['Documento de baja']

                    if objeto.OBSERVACIONES_BAJA != row['Observaciones de baja']:
                        modificado = True
                        objeto.OBSERVACIONES_BAJA = row['Observaciones de baja']
                    
                    if pd.notna(row['Fecha de baja del documento']):
                        if objeto.FECHA_BAJA_DOCUMENTO is not None:
                            fecha_objeto_baja_documento = pd.to_datetime(objeto.FECHA_BAJA_DOCUMENTO).strftime('%Y-%m-%d')
                            fecha_baja_documento = transformar_fecha(request, (row['Fecha de baja del documento']), 'Fecha de baja del documento', row)
                            if fecha_objeto_baja_documento != fecha_baja_documento:
                                modificado = True
                                objeto.FECHA_BAJA_DOCUMENTO = row['Fecha de baja del documento']
                        else:
                            modificado = True
                            objeto.FECHA_BAJA_DOCUMENTO = row['Fecha de baja del documento']
                    
                    if objeto.usuario != request.user:
                       objeto.usuario = request.user
                    
                    if modificado:
                        try:
                            objeto.full_clean()
                            objeto.save()
                            messages.success(request, f"Armamento con matricula {row['Matrícula']} fue actualizado exitosamente")
                        except ValidationError as e:
                            mensaje_error = str(e)
                            messages.error(request, f"Error al modificar el Armamento {objeto.MATRICULA}: {mensaje_error} en la fila {int(row.name) +2}")
                            return redirect('armamento_excel')
                    else:
                        messages.success(request, f"Armamento con matricula {row['Matrícula']} ya existia")
                    
                except Armamento.DoesNotExist:    
                # Si la fila no existe, crear un nuevo objeto
                    nuevo_objeto = Armamento(ID_ARMA = fila_id_arma, 
                                           INSTITUCION = fila_institucion, 
                                           DEPENDENCIA = fila_dependencia, 
                                           ENTIDAD = fila_entidad,
                                           MUNICIPIO = fila_municipio,
                                           NUMERO_LOC = fila_loc,
                                           FOLIO_C = row['Folio C'],
                                           FOLIO_D = row['Folio D'],
                                           CLASE_TIPO_ARMA = fila_ClaseTipoArma,
                                           CALIBRE_ARMA = fila_calibre,
                                           MARCA_ARMA = fila_marca,
                                           MODELO_ARMA = fila_modelo,
                                           MATRICULA = row['Matrícula'],
                                           MATRICULA_CANON = row['Matricula_canon *'],
                                           FECHA = fila_fecha_registro,
                                           FECHA_LOC = fila_fecha_loc,
                                           ESTADO_ARMA = fila_edoConservacion,
                                           FECHA_CAPTURA = fila_fecha_captura,
                                           OBSERVACIONES = row['Observaciones'],
                                           ESTATUS_ARMA = fila_estatus,
                                           CUIP_PORTADOR = row['CUIP del elemento que la porta'],
                                           CUIP_RESPONSABLE = row['CUIP del elemento que la porta'],
                                           CIHB = row['Código de Identificación de Huella Balística (CIHB)'],
                                           TIPO_FUNCIONAMIENTO = fila_tipoFuncionamiento,
                                           PROPIEDAD = fila_propiedad,
                                           FECHA_BAJA_LOGICA = fila_fecha_baja_logica,
                                           MOTIVO_BAJA = row['Motivo de baja'],
                                           DOCUMENTO_BAJA = row['Documento de baja'],
                                           OBSERVACIONES_BAJA = row['Observaciones de baja'],
                                           FECHA_BAJA_DOCUMENTO = fila_fecha_baja_documento,
                                           usuario = request.user     
                                           )  
                    
                    try:
                        nuevo_objeto.full_clean()
                        nuevo_objeto.save()
                    except ValidationError as e:
                        mensaje_error = str(e)
                        messages.error(request, f"Error al guardar el Armamento {nuevo_objeto.MATRICULA}: {mensaje_error} en la fila {int(row.name) +2}")
                        return redirect('armamento_excel')
                    messages.success(request, f"Armamento con matricula {row['Matrícula']} fue agregado con exito")

            return render(request, 'excel_armamento.html',{
                'form':form
            })
    else:
        form = ExcelUploadForm()
    return render(request, 'excel_armamento.html',{
        'form': form
    })

def validar_plantilla_excel(request, archivo_excel):
    try:
        # Lee el archivo Excel
        df = pd.read_excel(archivo_excel, engine="openpyxl")
        
        # Lista de nombres de columnas requeridas
        columnas_requeridas = [
            'ID Arma', 'Institución', 'Dependencia', 'Entidad', 'Municipio',
            'Número de licencia oficial colectiva', 'Folio C', 'Folio D',
            'Clase/Tipo de arma', 'Calibre del arma', 'Marca del arma',
            'Modelo del arma', 'Matrícula', 'Matricula_canon *', 'Fecha de registro',
            'Fecha de alta en la LOC', 'Estado del arma', 'Fecha de alta/captura',
            'Observaciones', 'Estatus del arma', 'CUIP del elemento que la porta',
            'CUIP del elemento responsable del cargo', 'Código de Identificación de Huella Balística (CIHB)',
            'Tipo de Funcionamiento', 'Propiedad', 'Fecha de baja logica', 'Motivo de baja',
            'Documento de baja', 'Observaciones de baja', 'Fecha de baja del documento',
        ]
        
        # Verifica si todas las columnas requeridas están presentes
        if all(columna in df.columns for columna in columnas_requeridas):
            return df
        else:
            messages.error(request, "El archivo no cumple con la plantilla requerida. Faltan columnas.")
            return None
    except pd.errors.EmptyDataError:
        messages.error(request, "El archivo está vacío o no es un archivo Excel válido.")
        return None
    except Exception as e:
        messages.error(request, f"Error al procesar el archivo: {e}")
        return None

@login_required
def ver_armamento(request, id):
    armamento = get_object_or_404(Armamento, pk=id)
    armamento = convertir_fechas(armamento)
    form = ArmamentoForm(instance=armamento)
        # Itera sobre los campos del formulario y establece el atributo "readonly" en True
    for field_name, field in form.fields.items():
        form.fields[field_name].disabled = True
    return render(request, 'ver_armamento.html', {'form': form,
                                                  'id': id})

@login_required
def editar_armamento(request, id):
    armamento = get_object_or_404(Armamento, pk=id)
    
    if request.method == 'POST':
        form = ArmamentoForm(request.POST, instance=armamento)
        if form.is_valid():
            objecto = form.save(commit=False)
            objecto.usuario = request.user
            objecto.save()
            messages.success(request, 'El Armamento fue editado exitosamente.')
            return redirect('armamento')
        else:
            return render(request, 'crear_armamento.html', {
                'form': form,
                'is_editing': True
            })
    else:
        armamento = convertir_fechas(armamento)
        form = ArmamentoForm(instance=armamento)

    return render(request, 'editar_armamento.html', {
        'form': form,
        'is_editing': True 
        })
   
@login_required
def eliminar_armamento(request, id):
    try:
        #Obtiene el registro por su ID, si no existe, lanzará una excepción 404
        registro = get_object_or_404(Armamento, pk=id)
        
        #Actualiza el campo usuario de quien lo elimino
        Armamento.objects.filter(pk=id).update(usuario=request.user)
        
        # Borra el registro
        registro.delete()
        
    except Exception as e:
        # Si ocurre una excepción, maneja el error apropiadamente
        messages.info(request, 'Error al eliminar: No se puede eliminar este armamento ya que se encuentra referenciada a una imagen.')
        return redirect('armamento')
    
    messages.info(request, 'El Armamento fue eliminado exitosamente.')      
    return redirect('armamento')  # Redirige a la misma vista  

@login_required
def reactivar_armamento(request, id):
    armamento = get_object_or_404(Armamento, pk=id)
    armamento.FECHA_BAJA_LOGICA = None
    armamento.MOTIVO_BAJA = None
    armamento.DOCUMENTO_BAJA = None
    armamento.OBSERVACIONES_BAJA = None
    armamento.FECHA_BAJA_DOCUMENTO = None
    armamento.save()
    messages.success(request, 'El Armamento fue reactivado exitosamente.')
    return redirect('armamento_activos')

@login_required
def baja_armamento(request, id):
    armamento = get_object_or_404(Armamento, pk=id)
    
    if request.method == 'POST':
        form = BajaArmamentoForm(request.POST, instance=armamento)
        if form.is_valid():
            objecto = form.save(commit=False)
            objecto.usuario = request.user
            objecto.save()
            messages.success(request, 'El Armamento fue dado de baja exitosamente.')
            return redirect('armamento_inactivos')
        else:
            return render(request, 'formBaja_armamento.html', {
                'form': form,
                'is_editing': True
            })
    else:
        armamento = convertir_fechas(armamento)
        form = BajaArmamentoForm(instance=armamento)

    return render(request, 'formBaja_armamento.html', {
        'form': form,
        'is_editing': True 
        })

def convertir_fechas(objeto):
    if objeto.FECHA: objeto.FECHA = objeto.FECHA.strftime("%Y-%m-%d")
    if objeto.FECHA_LOC: objeto.FECHA_LOC = objeto.FECHA_LOC.strftime("%Y-%m-%d")
    if objeto.FECHA_CAPTURA: objeto.FECHA_CAPTURA = objeto.FECHA_CAPTURA.strftime("%Y-%m-%d")
    if objeto.FECHA_BAJA_LOGICA: objeto.FECHA_BAJA_LOGICA= objeto.FECHA_BAJA_LOGICA.strftime("%Y-%m-%d")
    if objeto.FECHA_BAJA_DOCUMENTO: objeto.FECHA_BAJA_DOCUMENTO = objeto.FECHA_BAJA_DOCUMENTO.strftime("%Y-%m-%d")
    return objeto

@login_required
def obtener_municipios(request, entidad_id):
    try:
        municipios = Municipio.objects.filter(ID_ENTIDAD__ID_ENTIDAD=entidad_id).values('id', 'MUNICIPIO')

        return JsonResponse(list(municipios), safe=False)

    except Municipio.DoesNotExist:
        # Manejo de error si no se encuentra la entidad o no existen municipios asociados
        return JsonResponse([], safe=False)

@login_required
def obtener_instituciones(request, dependencia_id):
    try:
        instituciones = Institucion.objects.filter(ID_DEPENDENCIA=dependencia_id).values('ID_INSTITUCION', 'NOMBRE')

        return JsonResponse(list(instituciones), safe=False)

    except Institucion.DoesNotExist:
        # Manejo de error si no se encuentra o no existen instituciones asociadas
        return JsonResponse([], safe=False)   

@login_required
def descargar_plantilla_excel(request):
    ruta_plantilla = "static/plantillas/armamento_plantilla.xlsx"
    # Abre el archivo y devuelve una respuesta de archivo para descargar
    return FileResponse(open(ruta_plantilla, 'rb'), as_attachment=True)

def transformar_fecha(request, valor_fecha, columna, row):
    columnas_obligatorias = ['Fecha de registro', 'Fecha de alta en la LOC','Fecha de alta/captura']  # Lista de columnas que deben contener fechas
    try:
        # Verificar si la celda está vacía
        if pd.isna(valor_fecha):
            if columna in columnas_obligatorias:
                raise ValidationError(f"La fecha de la columna {columna} no puede estar vacía en la fila {int(row.name) + 2}")
            else:
                return None
        # Convertir la fecha al formato deseado
        fecha = pd.to_datetime(valor_fecha, errors='coerce')
    
        fecha_transformada = fecha.strftime('%Y-%m-%d')
        return fecha_transformada  # Devolver la fecha transformada como cadena

    except Exception as e:
        msj = f"Error en la columna {columna}: ({str(e)}) en la fila {int(row.name) + 2}"
        raise ValidationError(msj)

def transformar_numero(request, campo, row, columna):

    try:
        # Verificar si la celda está vacía
        if pd.isna(campo) or campo is None:
                return None
        # Convertir la fecha al formato deseado
        valor_str = str(campo)
        valor_float = float(valor_str)
        return int(valor_float)  # Devolver el numero 

    except Exception as e:
        msj = f"Error: Número invalido en {columna} en la fila {int(row.name) + 2},,,, {e}"
        raise ValidationError(msj)     

def obtener_institucion_id(request, cell_value):
    # Verificar si el valor es texto o número
    if isinstance(cell_value, str):
        # Es texto, hacer una consulta por nombre
        try:
            institucion = Institucion.objects.get(NOMBRE=cell_value)
            return institucion
        except Institucion.DoesNotExist:
            messages.error(request, f"No se encontró una institución con el nombre: '{cell_value}'")
            return None
    elif isinstance(cell_value, (int, float)):
        # Es número, hacer una consulta por id
        try:
            institucion = Institucion.objects.get(ID_INSTITUCION=cell_value)
            return institucion
        except Institucion.DoesNotExist:
            messages.error(request, f"No se encontró una institución con el id: '{cell_value}'")
            return None
    else:
        messages.error(request, f"El valor proporcionado en Institución no es ni texto ni número")
        return None
    
def obtener_dependencia_id(request, cell_value):
    # Verificar si el valor es texto o número
    if isinstance(cell_value, str):
        # Es texto, hacer una consulta por nombre
        try:
            dependencia = Dependencia.objects.get(DEPENDENCIA=cell_value)
            return dependencia
        except Dependencia.DoesNotExist:
            messages.error(request, f"No se encontró una Dependencia con el nombre: '{cell_value}'")
            return None
    elif isinstance(cell_value, (int, float)):
        # Es número, hacer una consulta por id
        try:
            dependencia = Dependencia.objects.get(ID_DEPENDENCIA=cell_value)
            return dependencia
        except Dependencia.DoesNotExist:
            messages.error(request, f"No se encontró una Dependencia con el id: '{cell_value}'")
            return None
    else:
        messages.error(request, f"El valor proporcionado de Dependencia no es ni texto ni número")
        return None
    
def obtener_entidad_id(request, cell_value):
    # Verificar si el valor es texto o número
    if isinstance(cell_value, str):
        # Es texto, hacer una consulta por nombre
        try:
            entidad = Entidad.objects.get(ENTIDAD=cell_value)
            return entidad
        except Entidad.DoesNotExist:
            messages.error(request, f"No se encontró una Entidad con el nombre: '{cell_value}'")
            return None
    elif isinstance(cell_value, (int, float)):
        # Es número, hacer una consulta por id
        try:
            entidad = Entidad.objects.get(ID_ENTIDAD=cell_value)
            return entidad
        except Dependencia.DoesNotExist:
            messages.error(request, f"No se encontró una Entidad con el id: '{cell_value}'")
            return None
    else:
        messages.error("El valor proporcionado para Entidad no es ni texto ni número")
        return None

def obtener_municipio_id(request, cell_value, entidad):
    # Verificar si el valor es texto o número
    if isinstance(cell_value, str):
        # Es texto, hacer una consulta por nombre
        try:
            municipio = Municipio.objects.get(MUNICIPIO=cell_value, ID_ENTIDAD=entidad)
            return municipio
        except Municipio.DoesNotExist:
            messages.error(request, f"No se encontró una Municipio con el nombre: '{cell_value}'")
            return None
    elif isinstance(cell_value, (int, float)):
        # Es número, hacer una consulta por id
        try:
            municipio = Municipio.objects.get(ID_MUNICIPIO=cell_value, ID_ENTIDAD=entidad)
            return municipio
        except Municipio.DoesNotExist:
            messages.error(request, f"No se encontró una Municipio con el id: '{cell_value}'")
            return None
    else:
        messages.error("El valor proporcionado para Municipio no es ni texto ni número")
        return None

def obtener_loc_id(request, cell_value):
    # Verificar si el valor es texto o número
    if isinstance(cell_value, str):
        # Es texto, hacer una consulta por nombre
        try:
            loc = LOC.objects.get(NO_LICENCIA=cell_value)
            return loc
        except LOC.DoesNotExist:
            messages.error(request, f"No se encontró un LOC con el nombre: '{cell_value}'")
            return None
    elif isinstance(cell_value, (int, float)):
        # Es número, hacer una consulta por id
        try:
            loc = LOC.objects.get(NO_LICENCIA=cell_value)
            return loc
        except LOC.DoesNotExist:
            messages.error(request, f"No se encontró un LOC con el nombre: '{cell_value}'")
            return None
    else:
        print("El valor proporcionado no es ni texto ni número")
        return None
    
def obtener_claseTipoArma_id(request, cell_value):
    # Verificar si el valor es texto o número
    if isinstance(cell_value, str):
        # Es texto, hacer una consulta por nombre
        try:
            clase = Tipo.objects.get(TIPO=cell_value)
            return clase
        except Tipo.DoesNotExist:
            messages.error(request, f"No se encontró un Tipo/Clase de arma con el nombre: '{cell_value}'")
            return None
    elif isinstance(cell_value, (int, float)):
        # Es número, hacer una consulta por id
        try:
            clase = Tipo.objects.get(ID_TIPO=cell_value)
            return clase
        except Tipo.DoesNotExist:
            messages.error(request, f"No se encontró un Tipo/Clase de arma con el id: '{cell_value}'")
            return None
    else:
        messages.error("El valor proporcionado para el Tipo/Clase de arma no es ni texto ni número")
        return None

def obtener_calibre_id(request, cell_value):
     # Verificar si el valor es texto o número
    if isinstance(cell_value, str):
        # Es texto, hacer una consulta por nombre
        try:
            calibre = Calibre.objects.get(CALIBRE=cell_value)
            return calibre
        except Calibre.DoesNotExist:
            messages.error(request, f"No se encontró un Calibre con el nombre: '{cell_value}'")
            return None
    elif isinstance(cell_value, (int, float)):
        # Es número, hacer una consulta por id
        try:
            calibre = Calibre.objects.get(ID_CALIBRE=cell_value)
            return calibre
        except Calibre.DoesNotExist:
            messages.error(request, f"No se encontró un Calibre con el id: '{cell_value}'")
            return None
    else:
        messages.error("El valor proporcionado para el Calibre no es ni texto ni número")
        return None

def obtener_marca_id(request,cell_value):
    # Verificar si el valor es texto o número
    if isinstance(cell_value, str):
        # Es texto, hacer una consulta por nombre
        try:
            marca = Marca.objects.get(MARCA=cell_value)
            return marca
        except Marca.DoesNotExist:
            messages.error(request, f"No se encontró una Marca con el nombre: '{cell_value}'")
            return None
    elif isinstance(cell_value, (int, float)):
        # Es número, hacer una consulta por id
        try:
            marca = Marca.objects.get(ID_MARCA=cell_value)
            return marca
        except Marca.DoesNotExist:
            messages.error(request, f"No se encontró una Marca con el id: '{cell_value}'")
            return None
    else:
        messages.error("El valor proporcionado para Marca no es ni texto ni número")
        return None

def obtener_modelo_id(request, cell_value):
    # Verificar si el valor es texto o número
    if isinstance(cell_value, str):
        # Es texto, hacer una consulta por nombre
        try:
            modelo = Modelo.objects.get(MODELO=cell_value)
            return modelo
        except Modelo.DoesNotExist:
            messages.error(request, f"No se encontró un Modelo con el nombre: '{cell_value}'")
            return None
    elif isinstance(cell_value, (int, float)):
        # Es número, hacer una consulta por id
        try:
            modelo = Modelo.objects.get(ID_MODELO=cell_value)
            return modelo
        except Modelo.DoesNotExist:
            messages.error(request, f"No se encontró un Modelo con el id: '{cell_value}'")
            return None
    else:
        messages.error("El valor proporcionado para Modelo no es ni texto ni número")
        return None

def obtener_edoConservacion_id(request, cell_value):
    # Verificar si el valor es texto o número
    if isinstance(cell_value, str):
        # Es texto, hacer una consulta por nombre
        try:
            edoConservacion = Edo_conservacion.objects.get(DESCRIPCION=cell_value)
            return edoConservacion
        except Edo_conservacion.DoesNotExist:
            messages.error(request, f"No se encontró un Estado de conservación con el nombre: '{cell_value}'")
            return None
    elif isinstance(cell_value, (int, float)):
        # Es número, hacer una consulta por id
        try:
            edoConservacion = Edo_conservacion.objects.get(ID_ESTADO=cell_value)
            return edoConservacion
        except Edo_conservacion.DoesNotExist:
            messages.error(request, f"No se encontró un Estado de conservación con el id: '{cell_value}'")
            return None
    else:
        messages.error("El valor proporcionado para Edo. de Conservación no es ni texto ni número")
        return None  
    
def obtener_statusArma_id(request, cell_value):
    # Verificar si el valor es texto o número
    if isinstance(cell_value, str):
        # Es texto, hacer una consulta por nombre
        try:
            statusArma = Estatus_Arma.objects.get(DESCRIPCION=cell_value)
            return statusArma
        except Estatus_Arma.DoesNotExist:
            messages.error(request, f"No se encontró un Estatus de arma con el nombre: '{cell_value}'")
            return None
    elif isinstance(cell_value, (int, float)):
        # Es número, hacer una consulta por id
        try:
            statusArma = Estatus_Arma.objects.get(ID_ESTATUS=cell_value)
            return statusArma
        except Estatus_Arma.DoesNotExist:
            messages.error(request, f"No se encontró un Estatus de arma con el id: '{cell_value}'")
            return None
    else:
        messages.error("El valor proporcionado para Estatus de Arma no es ni texto ni número")
        return None    

def obtener_propiedad_id(request, cell_value):
    # Verificar si el valor es texto o número
    if isinstance(cell_value, str):
        # Es texto, hacer una consulta por nombre
        try:
            propiedad = Propiedad.objects.get(Propiedad=cell_value)
            return propiedad
        except Propiedad.DoesNotExist:
            messages.error(request, f"No se encontró una Propiedad con el nombre: '{cell_value}'")
            return None
    elif isinstance(cell_value, (int, float)):
        # Es número, hacer una consulta por id
        try:
            propiedad = Propiedad.objects.get(ID=cell_value)
            return propiedad
        except Propiedad.DoesNotExist:
            messages.error(request, f"No se encontró una Propiedad con el id: '{cell_value}'")
            return None
    else:
        messages.error("El valor proporcionado no es ni texto ni número")
        return None 
    
def obtener_tipoFuncionamiento_id(request, cell_value):
    # Verificar si el valor es texto o número
    if isinstance(cell_value, str):
        # Es texto, hacer una consulta por nombre
        try:
            tipoFuncionamiento = TipoFuncinamiento.objects.get(TipoFuncionamiento=cell_value)
            return tipoFuncionamiento
        except TipoFuncinamiento.DoesNotExist:
            messages.error(request, f"No se encontró un Tipo de funcionamiento con el nombre: '{cell_value}'")
            return None
    elif isinstance(cell_value, (int, float)):
        # Es número, hacer una consulta por id
        try:
            tipoFuncionamiento = TipoFuncinamiento.objects.get(ID=cell_value)
            return tipoFuncionamiento
        except TipoFuncinamiento.DoesNotExist:
            messages.error(request, f"No se encontró un Tipo de funcionamiento con el id: '{cell_value}'")
            return None
    else:
        messages.error("El valor proporcionado para Tipo de funcionamiento no es ni texto ni número")
        return None