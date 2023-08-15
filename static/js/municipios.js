$(document).ready(function () {
    // Cuando cambia la selección del campo "Entidad"
    $('#id_ENTIDAD').change(function () {
        const entidadId = $(this).val();
        const municipioSelect = $('#id_MUNICIPIO');

        // Habilita el campo "Municipio" para permitir la selección
        municipioSelect.prop('disabled', false);

        // Realiza una solicitud AJAX para obtener los municipios filtrados por entidad
        $.ajax({
            url: `/armamento/obtener_municipios/${entidadId}/`, 
            
            // Utiliza el ID de entidad seleccionado en la URL
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                // Limpia los municipios existentes y agrega los nuevos basados en la respuesta JSON
                municipioSelect.empty();
                $.each(data, function (index, municipio) {
                    municipioSelect.append(new Option(municipio.MUNICIPIO, municipio.id));
                });
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});