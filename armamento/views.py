import datetime
from django.forms import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Armamento
from .forms import ArmamentoForm, BusquedaArmamentoForm, ExcelUploadForm
from django.contrib.auth.decorators import login_required
from .models import Municipio, Institucion, Dependencia, Entidad, LOC, Tipo, Calibre, Marca, Modelo, Edo_conservacion, Estatus_Arma
from django.contrib import messages
from utilidades import utils
import pandas as pd
from django.contrib import messages

# Create your views here.
@login_required
def armamento(request):
    armamentos = Armamento.objects.all().order_by('-ultima_modificacion')
    
    query = request.GET.get('query')
    valor = request.GET.get('campos_filtrados')
    
    if query and valor:
        return utils.BusquedaPersonalizada(request, query, valor, armamentos, 'armamento.html', BusquedaArmamentoForm)
        
    return utils.CrearPaginador(request, armamentos, 5, 'armamento.html', BusquedaArmamentoForm)

@login_required
def crear_armamento(request):
    if request.method == 'POST':
        form = ArmamentoForm(request.POST)
        if form.is_valid():
            objecto = form.save(commit=False)
            objecto.usuario = request.user
            objecto.save()
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
            df = pd.read_excel(archivo_excel, engine='openpyxl')
            
            # Reemplazar NaN por 0 en columnas numéricas
            df['ID Arma'] = df['ID Arma'].fillna(0)
            df['Matricula_canon *'] = df['Matricula_canon *'].fillna("")
            df['Código de Identificación de Huella Balística (CIHB)'] = df['Código de Identificación de Huella Balística (CIHB)'].fillna("")
            

            
            #Convirtiendo las columnas al tipo de dato esperado
            df['ID Arma'] = pd.to_numeric(df['ID Arma'], errors='coerce')
            df['Institución'] = pd.to_numeric(df['Institución'], errors='coerce')
            df['Dependencia'] = pd.to_numeric(df['Dependencia'], errors='coerce')
            df['Entidad'] = pd.to_numeric(df['Entidad'], errors='coerce')
            df['Municipio'] = pd.to_numeric(df['Municipio'], errors='coerce')
            df['Clase/Tipo de arma'] = pd.to_numeric(df['Clase/Tipo de arma'], errors='coerce')
            df['Calibre del arma'] = pd.to_numeric(df['Calibre del arma'], errors='coerce')
            df['Marca del arma'] = pd.to_numeric(df['Marca del arma'], errors='coerce')
            df['Modelo del arma'] = pd.to_numeric(df['Modelo del arma'], errors='coerce')
            df['Estado del arma'] = pd.to_numeric(df['Estado del arma'], errors='coerce')
            df['Estatus del arma'] = pd.to_numeric(df['Estatus del arma'], errors='coerce')
            df['Tipo de funcionamiento'] = pd.to_numeric(df['Tipo de funcionamiento'], errors='coerce')
            df['Fecha de registro'] = pd.to_datetime(df['Fecha de registro']).dt.strftime('%Y-%m-%d')
            df['Fecha de alta/captura'] = pd.to_datetime(df['Fecha de alta/captura']).dt.strftime('%Y-%m-%d')
            df['Fecha de alta en la LOC'] = pd.to_datetime(df['Fecha de alta en la LOC']).dt.strftime('%Y-%m-%d')
            
            
            
            
            for index, row in df.iterrows():
 
                #Convertimos los ids de los campos al excel a objetos para manejarlos
                fila_institucion = Institucion.objects.get(ID_INSTITUCION=row['Institución'])
                fila_dependencia = Dependencia.objects.get(ID_DEPENDENCIA=row['Dependencia'])
                fila_municipio = Municipio.objects.get(ID_ENTIDAD=row['Entidad'], ID_MUNICIPIO=row['Municipio'])
                fila_entidad = Entidad.objects.get(ID_ENTIDAD=row['Entidad'])
                fila_loc = LOC.objects.get(NO_LICENCIA=row['Número de licencia oficial colectiva'])
                fila_ClaseTipoArma = Tipo.objects.get(ID_TIPO=row['Clase/Tipo de arma'])
                fila_calibre = Calibre.objects.get(ID_CALIBRE=row['Calibre del arma'])
                fila_marca = Marca.objects.get(ID_MARCA=row['Marca del arma'])
                fila_modelo = Modelo.objects.get(ID_MODELO=row['Modelo del arma'])
                fila_edoConservacion = Edo_conservacion.objects.get(ID_ESTADO=row['Estado del arma'])
                fila_estatus = Estatus_Arma.objects.get(ID_ESTATUS=row['Estatus del arma'])
                
                 # Verificar si la fila ya existe en la base de datos
                try:
                    objeto = Armamento.objects.get(MATRICULA=row['Matrícula'])
                    modificado=False 
                    # Verificar si existen diferencias en los campos y actualizar si es necesario
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
                    
                    if objeto.ID_ARMA != row['ID Arma']:
                        modificado = True
                        objeto.ID_ARMA = row['ID Arma']
                    
                    if objeto.MATRICULA_CANON != row['Matricula_canon *']:
                        modificado = True
                        objeto.MATRICULA_CANON = row['Matricula_canon *']   
                    
                    if objeto.FECHA != row['Fecha de registro']:
                        objeto.FECHA = row['Fecha de registro'] 
                    
                    if objeto.FECHA_LOC != row['Fecha de alta en la LOC']:
                        objeto.FECHA_LOC = row['Fecha de alta en la LOC']
                    
                    if objeto.ESTADO_ARMA != fila_edoConservacion:
                        modificado = True
                        objeto.ESTADO_ARMA = fila_edoConservacion
                        
                    if objeto.FECHA_CAPTURA != row['Fecha de alta/captura']:
                        objeto.FECHA_CAPTURA = row['Fecha de alta/captura']
                    
                    if objeto.OBSERVACIONES != row['Observaciones']:
                        modificado = True
                        objeto.OBSERVACIONES = row['Observaciones']
                    
                    if objeto.ESTATUS_ARMA != fila_estatus:
                        modificado = True
                        objeto.ESTATUS_ARMA = fila_estatus
                        
                    if objeto.CUIP_PORTADOR != row['CUIP del elemento que la porta']:
                        modificado = True
                        objeto.CUIP_PORTADOR = row['CUIP del elemento que la porta']
                    
                    if objeto.CUIP_RESPONSABLE != row['CUIP del elemento que la porta']:
                        modificado = True
                        objeto.CUIP_RESPONSABLE = row['CUIP del elemento que la porta']
                    
                    if objeto.CIHB != row['Código de Identificación de Huella Balística (CIHB)']:
                        modificado = True
                        objeto.CIHB = row['Código de Identificación de Huella Balística (CIHB)']
                        
                    if objeto.TIPO_FUNCIONAMIENTO != row['Tipo de funcionamiento']:
                        modificado = True
                        objeto.TIPO_FUNCIONAMIENTO = row['Tipo de funcionamiento']
                    
                    if objeto.usuario != request.user:
                       objeto.usuario = request.user
                    
                    try:
                        objeto.full_clean()
                        objeto.save()
                    except ValidationError as e:
                        mensaje_error = str(e)
                        messages.error(request, f"Error al guardar el Armamento {objeto.MATRICULA}: {mensaje_error}")
                        return redirect('armamento_excel')
                    
                    if modificado:
                        messages.success(request, f"Armamento con matricula {row['Matrícula']} fue actualizado exitosamente")
                    else:
                        messages.success(request, f"Armamento con matricula {row['Matrícula']} ya existia")

                    
                except Armamento.DoesNotExist:
                # Si la fila no existe, crear un nuevo objeto
                    nuevo_objeto = Armamento(ID_ARMA = row['ID Arma'], 
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
                                           FECHA = row['Fecha de registro'],
                                           FECHA_LOC = row['Fecha de alta en la LOC'],
                                           ESTADO_ARMA = fila_edoConservacion,
                                           FECHA_CAPTURA = row['Fecha de alta/captura'],
                                           OBSERVACIONES = row['Observaciones'],
                                           ESTATUS_ARMA = fila_estatus,
                                           CUIP_PORTADOR = row['CUIP del elemento que la porta'],
                                           CUIP_RESPONSABLE = row['CUIP del elemento que la porta'],
                                           CIHB = row['Código de Identificación de Huella Balística (CIHB)'],
                                           TIPO_FUNCIONAMIENTO = row['Tipo de funcionamiento'],
                                        #    FECHA_BAJA_LOGICA = row['Fecha de baja logica'],
                                        #    MOTIVO_BAJA = row['Motivo de baja'],
                                        #    DOCUMENTO_BAJA = row['Documento de baja'],
                                        #    OBSERVACIONES_BAJA = row['Observaciones de baja'],
                                        #    FECHA_BAJA_DOCUMENTO = row['Fecha de baja del documento'],
                                           usuario = request.user     
                                           )  
                    
                    try:
                        nuevo_objeto.full_clean()
                        nuevo_objeto.save()
                    except ValidationError as e:
                        mensaje_error = str(e)
                        messages.error(request, f"Error al guardar el Armamento {nuevo_objeto.MATRICULA}: {mensaje_error}")
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

@login_required
def editar_armamento(request, id):
    armamento = get_object_or_404(Armamento, pk=id)
    
    if request.method == 'POST':
        form = ArmamentoForm(request.POST, instance=armamento)
        if form.is_valid():
            objecto = form.save(commit=False)
            objecto.usuario = request.user
            objecto.save()
            return redirect('armamento')
        else:
            print(form.errors)  # Mostrar errores en la consola
    else:
        armamento = convertir_fechas(armamento)
        form = ArmamentoForm(instance=armamento)

    return render(request, 'editar_armamento.html', {
        'form': form,
        'is_editing': True 
        })

def validate_fecha_1990(value):
    if value < datetime(1990, 1, 1).date():
        raise ValidationError('La fecha no puede ser anterior al 01 de enero de 1990.')
    
@login_required
def eliminar_armamento(request, id):
    try:
        #Obten el registro por su ID, si no existe, lanzará una excepción 404
        registro = get_object_or_404(Armamento, pk=id)
        
        #Actualiza el campo usuario de quien lo elimino
        Armamento.objects.filter(pk=id).update(usuario=request.user)
        
        # Borra el registro
        registro.delete()
        
    except Exception as e:
        # Si ocurre una excepción, maneja el error apropiadamente
        messages.error(request, f'Error al eliminar: No se puede eliminar este armamento ya que se encuentra referenciada a una imagen.')
        
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