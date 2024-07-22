document.addEventListener('DOMContentLoaded', function() {
    // Obtener listado de hoteles
    fetch('http://0.0.0.0:5000/lista-clientes')
        .then(response => response.json())
        .then(data => {
            const clienteSelect = document.getElementById('cliente');
            data.forEach(cliente => {
                const option = document.createElement('option');
                option.value = cliente.id;
                option.textContent = ` DNI: ${cliente.DNI} - Apellido: ${cliente.apellido}` ; 
                clienteSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error:', error));

    })

document.addEventListener('DOMContentLoaded', function() {
    // Obtener listado de hoteles
    fetch('http://0.0.0.0:5000/hoteles')
        .then(response => response.json())
        .then(data => {
            const hotelSelect = document.getElementById('hotel');
            data.forEach(hotel => {
                const option = document.createElement('option');
                option.value = hotel.id;
                option.textContent = hotel.nombre;
                hotelSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error:', error));

    // Actualizar habitaciones disponibles cuando se selecciona un hotel pero ahora tiene que sumar toda la info 
    document.getElementById('hotel').addEventListener('change', function() {
        const hotelId = this.value;
        fetch(`http://0.0.0.0:5000/habitaciones_disponibles/${hotelId}`)
            .then(response => response.json())
            .then(data => {
                const habitacionSelect = document.getElementById('habitacion');
                habitacionSelect.innerHTML = ''; // Limpiar opciones anteriores
                data.forEach(habitacion => {
                    const option = document.createElement('option');
                    option.value = habitacion.id;
                    option.textContent = `Habitación ${habitacion.numero} - ${habitacion.cant_personas} personas - Servicio: ${habitacion.service}`;
                    habitacionSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error:', error));
    });




});


