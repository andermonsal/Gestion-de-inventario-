async function cargarProductos() {
    try {
        const productos = await fetchAPI("/productos");
        const selectProducto = document.getElementById("producto-venta");
        selectProducto.innerHTML = '<option value="">Selecciona un producto</option>';
        productos.forEach(producto => {
            const opcion = document.createElement("option");
            opcion.value = JSON.stringify(producto);
            opcion.textContent = `${producto.nombre} ($${producto.precio})`;
            selectProducto.appendChild(opcion);
        });
    } catch (error) {
        alert("Error al cargar los productos: " + error.message);
    }
}

async function registrarVenta(evento) {
    evento.preventDefault();
    const productoSeleccionado = JSON.parse(document.getElementById("producto-venta").value);
    const cantidad = parseInt(document.getElementById("cantidad-venta").value);
    const venta = {
        productos: [{
            id: productoSeleccionado.id,
            cantidad: cantidad,
            precio: productoSeleccionado.precio
        }],
        id_empleado: localStorage.getItem("token")
    };
    try {
        await fetchAPI("/ventas", "POST", venta);
        alert("Venta registrada con éxito");
        document.getElementById("formulario-venta").reset();
    } catch (error) {
        alert("Error al registrar la venta: " + error.message);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    if (!estaAutenticado()) {
        window.location.href = "login.html";
        return;
    }
    cargarProductos();
    document.getElementById("formulario-venta").addEventListener("submit", registrarVenta);
});