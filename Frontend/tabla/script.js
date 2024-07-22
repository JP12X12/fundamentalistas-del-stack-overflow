function saveEdit(id, row) {
    const inputs = row.querySelectorAll("input");
    const data = {
        DNI: inputs[0].value,
        nombre: inputs[1].value,
        apellido: inputs[2].value,
        telefono: inputs[3].value,
        edad: inputs[4].value,
    };

    fetch(`/editar_cliente/${id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response_received)
    .then(data => {
        row.innerHTML = `
            <td>${data.DNI}</td>
            <td>${data.nombre}</td>
            <td>${data.apellido}</td>
            <td>${data.telefono}</td>
            <td>${data.edad}</td>
            <td>
                <button onclick="editRow(${id})">Editar</button>
                <a href="/tabla/delete/${id}">Eliminar</a>
            </td>
        `;
    })
    .catch(error => console.error('Error:', error));
}
