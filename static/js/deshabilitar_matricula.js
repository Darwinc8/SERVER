// Deshabilitar el campo select
document.getElementById('matricula').disabled = true;

// Habilitar el campo select antes de enviar el formulario
   function enableFieldAndSubmit(event) {
    event.preventDefault();
    document.getElementById('matricula').disabled = false;
    document.getElementById('myForm').submit();
}