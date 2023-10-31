
  $(document).ready(function() {
    // Almacenar los valores iniciales de los campos del formulario
    var initialData = {};
    $('#myForm input[type="text"], #myForm input[type="number"], #myForm select, #myForm input[type="file"]').each(function() {
      var fieldName = $(this).attr('name');
      console.log("Selected field name: ", fieldName);
      initialData[fieldName] = $(this).val();
    });

    // Función para comprobar si ha habido cambios en los campos
    function hasChanges() {
      var formData = {};
      $('#myForm input[type="text"], #myForm input[type="number"], #myForm select, #myForm input[type="file"]').each(function() {
        var fieldName = $(this).attr('name');
        console.log("Selected field name: ", fieldName);
        formData[fieldName] = $(this).val();
      });

      return JSON.stringify(initialData) !== JSON.stringify(formData);
    }

    // Habilitar/deshabilitar el botón de guardar según los cambios
    function toggleGuardarButton() {
      if (hasChanges()) {
        $('#guardar-btn').prop('disabled', false);
      } else {
        $('#guardar-btn').prop('disabled', true);
      }
    }

    // Escuchar los eventos de cambio en los campos del formulario
    $('#myForm input[type="text"], #myForm input[type="number"]').on('input', toggleGuardarButton);
    $('#myForm select').on('change', toggleGuardarButton);
    $('#myForm input[type="file"]').on('change', toggleGuardarButton);

    // Inicialmente, deshabilitar el botón de guardar si no hay cambios
    toggleGuardarButton();
  });