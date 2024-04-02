document.addEventListener('DOMContentLoaded', function() {
    var fileInput = document.getElementById('excel');
    var submitButton = document.getElementById('cargar_excel');

    fileInput.addEventListener('change', function() {
        if (fileInput.files.length > 0) {
            submitButton.disabled = false;
        } else {
            submitButton.disabled = true;
        }
    });
});