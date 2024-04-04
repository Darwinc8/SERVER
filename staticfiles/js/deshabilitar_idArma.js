// Deshabilitar el campo select
    document.getElementById('id_ID_ARMA').disabled = true;  
   
// Habilitar el campo select antes de enviar el formulario
   function enableFieldAndSubmit(event) {
    event.preventDefault();
    var selectField = document.getElementById('id_ID_ARMA');
    selectField.disabled = false;
    document.getElementById('myForm').submit();
}