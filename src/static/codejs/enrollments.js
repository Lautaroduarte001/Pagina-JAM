const selectCanciones = document.getElementById("song_select");
const fieldsetInstrumentos = document.getElementById("instrumentOptions");

fetch('/enrollment_data').then(response => {
    response.json().then(function(enrollments_data){
        const available_songs = enrollments_data["available_songs"];
        const available_instruments = enrollments_data["available_instruments"];

        for (const song in available_songs) {
            if (available_songs.hasOwnProperty(song)) {
                const option = document.createElement("option");
                option.value = song
                option.text = available_songs[song];
                selectCanciones.appendChild(option);
            }
        }

        selectCanciones.addEventListener('change', function(){
            const selectedSong= selectCanciones.value;
            const instruments = available_instruments[selectedSong];

            fieldsetInstrumentos.innerHTML = "";

            for (const instrument in instruments) {
                const radioInput = document.createElement("input");
                radioInput.type = "radio";
                radioInput.name = "instrument";
                radioInput.value = instruments[instrument];

                const label = document.createElement("label");
                label.textContent = instruments[instrument];
                label.classList.add("instrumento-label");

                fieldsetInstrumentos.appendChild(radioInput);
                fieldsetInstrumentos.appendChild(label);
            }
        });

        // Agregar el evento de clic a las etiquetas después de crearlas
        fieldsetInstrumentos.addEventListener('click', function(event) {
            if (event.target.classList.contains('instrumento-label')) {
                // Obtener el input asociado a esta etiqueta
                const input = event.target.previousElementSibling;
                
                // Verificar si el input ya está marcado
                if (!input.checked) {
                    // Si no está marcado, marcarlo
                    input.checked = true;
                } else {
                    // Si ya está marcado, desmarcarlo
                    input.checked = false;
                }
            }
        });

        const form = document.getElementById('registrationForm');
        form.addEventListener('submit', (event) => {
            const selectedInstrument = document.querySelector('input[name="instrument"]:checked');
            if (!selectedInstrument) {
                event.preventDefault();
                alert('Por favor, selecciona un instrumento.');
            }
        });

    });
});