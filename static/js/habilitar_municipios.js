function habilitarMunicipio() {
    var entidad = document.getElementById("id_ENTIDAD").value;
    var municipio = document.getElementById("id_MUNICIPIO");
    if (entidad && entidad.trim() !== "") {
        municipio.disabled = false;
    } else {
        municipio.disabled = true;
        municipio.value = "";
    }
}

// Llamamos a la función habilitarMunicipio() cuando cambia la selección en el campo "Entidad"
document.getElementById("id_ENTIDAD").addEventListener("change", habilitarMunicipio);
// Llamamos a la función al cargar la página para verificar si inicialmente debe estar deshabilitado
habilitarMunicipio();

// script.js