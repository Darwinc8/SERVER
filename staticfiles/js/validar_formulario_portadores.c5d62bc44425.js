function validarForm() {
    var inputQuery = document.getElementById('id_query');
    
    if (inputQuery.value.length < 3) {
        alert('El campo debe contener al menos 3 caracteres.');
        return false; // Evita que el formulario se envíe
    }
    
    return true; // Envía el formulario si la validación es exitosa
};
