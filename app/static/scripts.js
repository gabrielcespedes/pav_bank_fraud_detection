function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value; 

    if (username && password) {
        localStorage.setItem('username', username); 
        window.location.href = '/prediccion'; 
    } else {
        alert("Por favor, introduce tanto el usuario como la contraseña."); 
    }
}