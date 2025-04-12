async function cargarInventario() {
    try {
        const productos = await fetchAPI("/productos");
        const cuerpoTabla = document.querySelector("#tabla-inventario tbody");
        cuerpoTabla.innerHTML = "";
        productos.forEach(producto => {
            const fila = document.createElement("tr");
            fila.innerHTML = `
                <td>${producto.id}</td>
                <td>${producto.nombre}</td>
                <td>${producto.precio}</td>
                <td>${producto.cantidad}</td>
                <td>${producto.categoria}</td>
            `;
            cuerpoTabla.appendChild(fila);
        });
    } catch (error) {
        alert("Error al cargar el inventario: " + error.message);
    }
}

async function agregarProducto(evento) {
    evento.preventDefault();
    const producto = {
        id: document.getElementById("id-producto").value,
        nombre: document.getElementById("nombre-producto").value,
        precio: parseFloat(document.getElementById("precio-producto").value),
        cantidad: parseInt(document.getElementById("cantidad-producto").value),
        categoria: document.getElementById("categoria-producto").value,
        stock_minimo: parseInt(document.getElementById("stock-minimo").value)
    };
    try {
        await fetchAPI("/productos", "POST", producto);
        alert("Producto agregado con éxito");
        cargarInventario();
        document.getElementById("formulario-producto").reset();
    } catch (error) {
        alert("Error al agregar el producto: " + error.message);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    if (!estaAutenticado()) {
        window.location.href = "login.html";
        return;
    }
    if (obtenerRol() !== "admin") {
        document.getElementById("formulario-producto").style.display = "none";
    }
    cargarInventario();
    document.getElementById("formulario-producto")?.addEventListener("submit", agregarProducto);
});