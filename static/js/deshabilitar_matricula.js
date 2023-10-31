  $(document).ready(function() {
    // Deshabilitar la edición si el campo tiene un valor específico
    var matriculaField = $('#matricula-input');
    if (matriculaField.val()) {
      matriculaField.prop('readonly', true);
    }
  });