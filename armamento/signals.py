from django.utils import timezone
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from armamento.models import Armamento, ArmamentoLog

@receiver(post_save, sender=Armamento)
def despues_de_insertar(sender, instance, created, **kwargs):
    if created:
        estado = "Creación"
    else:
        estado = "Modificación"

    ArmamentoLog.objects.create(
        estado = estado,
        id_alterna = instance,
        id_arma = instance.ID_ARMA,
        institucion = instance.INSTITUCION,
        dependencia = instance.DEPENDENCIA,
        entidad = instance.ENTIDAD,
        municipio = instance.MUNICIPIO,
        numero_loc = instance.NUMERO_LOC,
        folio_c= instance.FOLIO_C,
        folio_d = instance.FOLIO_D,
        clase_tipo_arma = instance.CLASE_TIPO_ARMA,
        calibre_arma = instance.CALIBRE_ARMA,
        marca_arma = instance.MARCA_ARMA,
        modelo_arma = instance.MODELO_ARMA,
        matricula = instance.MATRICULA,
        matricula_canon = instance.MATRICULA_CANON,
        fecha = instance.FECHA,
        fecha_loc = instance.FECHA_LOC,
        estado_arma = instance.ESTADO_ARMA,
        fecha_captura = instance.FECHA_CAPTURA,
        observaciones = instance.OBSERVACIONES,
        estatus_arma = instance.ESTATUS_ARMA,
        cuip_portador = instance.CUIP_PORTADOR.CUIP,
        cuip_responsable = instance.CUIP_RESPONSABLE.CUIP,
        cihb = instance.CIHB,
        fecha_baja_logica = instance.FECHA_BAJA_LOGICA,
        motivo_baja = instance.MOTIVO_BAJA,
        documento_baja = instance.DOCUMENTO_BAJA,
        observaciones_baja = instance.OBSERVACIONES_BAJA,
        fecha_baja_documento = instance.FECHA_BAJA_DOCUMENTO,
        usuario = instance.usuario,
        ultima_modificacion = instance.ultima_modificacion
    )
    print("Copia de creación/Modificacíon creada...")

@receiver(pre_delete, sender=Armamento)
def antes_de_eliminar(sender, instance,**kwargs):
    ArmamentoLog.objects.create(
        estado = "Eliminación",
        id_alterna = instance,
        id_arma = instance.ID_ARMA,
        institucion = instance.INSTITUCION,
        dependencia = instance.DEPENDENCIA,
        entidad = instance.ENTIDAD,
        municipio = instance.MUNICIPIO,
        numero_loc = instance.NUMERO_LOC,
        folio_c= instance.FOLIO_C,
        folio_d = instance.FOLIO_D,
        clase_tipo_arma = instance.CLASE_TIPO_ARMA,
        calibre_arma = instance.CALIBRE_ARMA,
        marca_arma = instance.MARCA_ARMA,
        modelo_arma = instance.MODELO_ARMA,
        matricula = instance.MATRICULA,
        matricula_canon = instance.MATRICULA_CANON,
        fecha = instance.FECHA,
        fecha_loc = instance.FECHA_LOC,
        estado_arma = instance.ESTADO_ARMA,
        fecha_captura = instance.FECHA_CAPTURA,
        observaciones = instance.OBSERVACIONES,
        estatus_arma = instance.ESTATUS_ARMA,
        cuip_portador = instance.CUIP_PORTADOR.CUIP,
        cuip_responsable = instance.CUIP_RESPONSABLE.CUIP,
        cihb = instance.CIHB,
        fecha_baja_logica = instance.FECHA_BAJA_LOGICA,
        motivo_baja = instance.MOTIVO_BAJA,
        documento_baja = instance.DOCUMENTO_BAJA,
        observaciones_baja = instance.OBSERVACIONES_BAJA,
        fecha_baja_documento = instance.FECHA_BAJA_DOCUMENTO,
        usuario = instance.usuario,
        ultima_modificacion = timezone.now()
    )
    print("Copia de eliminación creada...")