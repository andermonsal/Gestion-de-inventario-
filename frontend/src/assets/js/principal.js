const URL_API = "http://localhost:8000";

async function fetchAPI(endpoint, metodo = "GET", cuerpo = null) {
    const token = localStorage.getItem("token");
    const opciones = {
        method: metodo,
        headers: {
            "Content-Type": "application/json",
            ...(token && { "Authorization": `Bearer ${token}` })
        },
        body: cuerpo ? JSON.stringify(cuerpo) : null
    };
    const respuesta = await fetch(`${URL_API}${endpoint}`, opciones);
    if (!respuesta.ok) {
        throw new Error(await respuesta.text());
    }
    return respuesta.json();
}

function estaAutenticado() {
    return !!localStorage.getItem("token");
}

function obtenerRol() {
    return localStorage.getItem("rol");
}

function cerrarSesion() {
    localStorage.removeItem("token");
    localStorage.removeItem("rol");
    window.location.href = "login.html";
}