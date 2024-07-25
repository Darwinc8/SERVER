document.addEventListener("DOMContentLoaded", function () {
    const botonesEliminar = document.querySelectorAll('.boton-borrar');

    botonesEliminar.forEach(function (deleteButton) {
        deleteButton.addEventListener("click", function () {
            const url = deleteButton.getAttribute("data-url");
            const confirmDelete = confirm("¿Estás seguro de que quieres dar de baja este armamento?");

            if (confirmDelete) {
                // Redirige a la URL de eliminación si se confirma
                window.location.href = url;
            }
        });
    });
});
