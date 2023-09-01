document.addEventListener("DOMContentLoaded", function () {
    const deleteButton = document.getElementById("boton-borrar");

    if (deleteButton) {
        deleteButton.addEventListener("click", function () {
            const url = deleteButton.getAttribute("data-url");
            const confirmDelete = confirm("¿Estás seguro de que quieres eliminar este registro?");

            if (confirmDelete) {
                // Redirige a la URL de eliminación si se confirma
                window.location.href = url;
            }
        });
    }
});