$(document).ready(function() {
    $('#id_CUIP_PORTADOR, #id_CUIP_RESPONSABLE').change(function() {
        var campo1Value = $('#id_CUIP_PORTADOR').val();
        var campo2Value = $('#id_CUIP_RESPONSABLE').val();
        
        if (campo1Value === campo2Value) {
            alert('El CUIP del responsable no puede ser el mismo que el CUIP del Portador');
            $('#id_CUIP_RESPONSABLE').val('');
        }
    });
});