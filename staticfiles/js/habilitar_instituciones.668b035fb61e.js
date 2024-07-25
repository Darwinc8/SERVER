// script.js
function habilitarInstitucion() {
    var dependencia = document.getElementById("id_DEPENDENCIA").value;
    var institucion = document.getElementById("id_INSTITUCION");
    if (dependencia && dependencia.trim() !== "") {
        institucion.disabled = false;
    } else {
        institucion.disabled = true;
        if (!institucion.value) {
            institucion.value = ""; // Limpiar el valor del campo Institución solo si está vacío
        }
    }
}

// Llamamos a la función habilitarInstitucion() cuando cambia la selección en el campo "Dependencia"
document.getElementById("id_DEPENDENCIA").addEventListener("change", habilitarInstitucion);
// Llamamos a la función al cargar la página para verificar si inicialmente debe estar deshabilitado
habilitarInstitucion();

