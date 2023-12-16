document.getElementById('calcular').addEventListener('click', function() {
    var presupuesto = document.getElementById('presupuesto').value;
    var maxRutas = document.getElementById('maxRutas').value;
    var resultadosDiv = document.getElementById('resultados');

    fetch('http://localhost:5000/optimize-routes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({presupuesto: parseInt(presupuesto, 10), max_rutas: parseInt(maxRutas, 10)})
    })
    .then(response => response.json())
    .then(data => {
        var html = '<h2>Rutas Seleccionadas:</h2>';
        data.forEach(ruta => {
            html += `ID Ruta: ${ruta['ID Ruta']}, Costo: ${ruta['Costo Operativo']}, Ganancia Neta: ${ruta['Ganancia Neta']}<br>`;
        });
        resultadosDiv.innerHTML = html;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
