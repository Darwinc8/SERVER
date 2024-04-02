$(document).ready(function () {
    // Cuando cambia la selección del campo "Dependencia"
    $('#id_DEPENDENCIA').change(function () {
        const dependenciaId = $(this).val();
        const institucionSelect = $('#id_INSTITUCION');

        // Habilita el campo "Institucion" para permitir la selección
        institucionSelect.prop('disabled', false);

        // Realiza una solicitud AJAX para obtener los municipios filtrados por entidad
        $.ajax({
            url: `/armamento/obtener_instituciones/${dependenciaId}/`, 
            
            // Utiliza el ID de la dependencia seleccionado en la URL
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                // Limpia las instituciones existentes y agrega los nuevos basados en la respuesta JSON
                institucionSelect.empty();
                $.each(data, function (index, institucion) {
                    institucionSelect.append(new Option(institucion.NOMBRE, institucion.ID_INSTITUCION));
                });
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});