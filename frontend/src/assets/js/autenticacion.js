async function iniciarSesion(evento) {
    evento.preventDefault();
    const nombre_usuario = document.getElementById("nombre_usuario").value;
    const contrasena = document.getElementById("contrasena").value;
    try {
        const respuesta = await fetchAPI("/login", "POST", { nombre_usuario, contrasena });
        localStorage.setItem("token", respuesta.token);
        localStorage.setItem("rol", respuesta.rol);
        window.location.href = "index.html";
    } catch (error) {
        alert("Error al iniciar sesión: " + error.message);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    if (estaAutenticado()) {
        window.location.href = "index.html";
    }
    document.getElementById("formulario-login").addEventListener("submit", iniciarSesion);
});