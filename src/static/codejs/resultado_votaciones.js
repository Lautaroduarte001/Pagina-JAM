fetch('/fetch_votes')
    .then(response => response.json())
    .then(function(data) {
        var votes_results = data;
        var canciones = Object.keys(votes_results);
        var resultados = Object.values(votes_results);

        var cancionesConResultados = canciones.map((cancion, index) => ({
            cancion: cancion,
            resultado: resultados[index]
        }));

        cancionesConResultados.sort((a, b) => b.resultado - a.resultado);
        resultados.sort((a, b) => b - a);

        var cancionesOrdenadas = cancionesConResultados.map(objeto => objeto.cancion);

        const ctx = document.getElementById('myChart');

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: cancionesOrdenadas,
                datasets: [{
                    axis: 'y',
                    label: 'Resultado Votaciones',
                    data: resultados,
                    borderWidth: 1
                }]
            },
            options: {
                indexAxis: 'y',
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    });