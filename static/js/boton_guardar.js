$(document).ready(function() {
    // Almacenar los valores iniciales de los campos del formulario
    var initialData = {};
    $('#myForm input[type="text"], #myForm input[type="email"], #myForm input[type="file"]').each(function() {
      initialData[this.name] = $(this).val();
    });
  
    // Función para comprobar si ha habido cambios en los campos
    function hasChanges() {
      var formData = {};
      $('#myForm input[type="text"], #myForm input[type="email"], #myForm input[type="file"]').each(function() {
        formData[this.name] = $(this).val();
      });
  
      return JSON.stringify(initialData) !== JSON.stringify(formData);
    }
  
    // Habilitar/deshabilitar el botón de guardar según los cambios
    function toggleGuardarButton() {
      if (hasChanges()) {
        $('#guardar-btn').removeClass('disabled');
      } else {
        $('#guardar-btn').addClass('disabled');
      }
    }
  
    // Escuchar los eventos de cambio en los campos del formulario
    $('#myForm input[type="text"], #myForm input[type="email"], #myForm input[type="file"]').on('input', toggleGuardarButton);
  
    // Inicialmente, deshabilitar el botón de guardar si no hay cambios
    toggleGuardarButton();
  });