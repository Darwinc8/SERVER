  $(document).ready(function() {

    // Capturar el evento de tecla "Enter" en los campos de entrada
    $('#myForm input[type="text"], #myForm input[type="number"]').on('keydown', function(event) {
      if (event.key === "Enter") {
        event.preventDefault();
        return false;
      }
    });
  });
