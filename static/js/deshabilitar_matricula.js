function enableFieldAndSubmit(event) {
    event.preventDefault(); // Prevenir el envío del formulario por defecto

    var field = document.getElementById('id_MATRICULA');
    field.disabled = false;
    console.log("hola")

    // Envía el formulario después de habilitar el campo
    document.getElementById('myForm').submit();
}