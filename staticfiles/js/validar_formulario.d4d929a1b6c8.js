function validarForm() {
    var inputQuery = document.getElementById('id_query');
    var inputCampoFiltrado = document.getElementById('id_campos_filtrados');
    var textoSeleccionado = inputCampoFiltrado.options[inputCampoFiltrado.selectedIndex].text;
    
    if (textoSeleccionado === "ID") {
        // Si la opción seleccionada es "ID", verifica si el valor contiene letras
        var contieneLetras = /[a-zA-Z]/.test(inputQuery.value);
        if (contieneLetras) {
            alert('El campo no debe contener letras cuando se selecciona "ID".');
            return false; // Evita que el formulario se envíe
        }
    } else {
        // Otra lógica de validación si la opción seleccionada no es "ID"
        if (inputQuery.value.length < 3) {
            alert('El campo debe contener al menos 3 caracteres.');
            return false; // Evita que el formulario se envíe
        }
    }
    
    return true; // Envía el formulario si la validación es exitosa
};
