// Mostrar el nombre del archivo seleccionado en prediccion.html
document.addEventListener('DOMContentLoaded', function () {
    const fileInput = document.getElementById('file');
    const fileNameDisplay = document.getElementById('file-name');

    if (fileInput && fileNameDisplay) {
        fileInput.addEventListener('change', function () {
            const fileName = this.files[0] ? this.files[0].name : 'Ningún archivo seleccionado';
            fileNameDisplay.textContent = fileName;
        });
    }
});