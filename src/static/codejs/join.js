const opcionesInstrumentos = {
    cancion1: [],
    cancion2: [],
    cancion3: [],
    cancion4: [],
    cancion5: [],
    cancion6: [],
    cancion7: [],
    cancion8: [],
    cancion9: [],
    cancion10: [],
    cancion11: [],
    // Agrega aquí las opciones para las demás canciones
};

const string_song1 = "{{cancion1}}";
const string_song2 = "{{cancion2}}";
const string_song3 = "{{cancion3}}";
const string_song4 = "{{cancion4}}";
const string_song5 = "{{cancion5}}";
const string_song6 = "{{cancion6}}";
const string_song7 = "{{cancion7}}";
const string_song8 = "{{cancion8}}";
const string_song9 = "{{cancion9}}";
const string_song10 = "{{cancion10}}";
const string_song11 = "{{cancion11}}";


// Reemplazar los caracteres especiales para obtener una cadena JSON válida
const json_string1 = string_song1.replace(/&#39;/g, '"').replace(/'/g, '"');
const json_string2 = string_song2.replace(/&#39;/g, '"').replace(/'/g, '"');
const json_string3 = string_song3.replace(/&#39;/g, '"').replace(/'/g, '"');
const json_string4 = string_song4.replace(/&#39;/g, '"').replace(/'/g, '"');
const json_string5 = string_song5.replace(/&#39;/g, '"').replace(/'/g, '"');
const json_string6 = string_song6.replace(/&#39;/g, '"').replace(/'/g, '"');
const json_string7 = string_song7.replace(/&#39;/g, '"').replace(/'/g, '"');
const json_string8 = string_song8.replace(/&#39;/g, '"').replace(/'/g, '"');
const json_string9 = string_song9.replace(/&#39;/g, '"').replace(/'/g, '"');
const json_string10 = string_song10.replace(/&#39;/g, '"').replace(/'/g, '"');
const json_string11 = string_song11.replace(/&#39;/g, '"').replace(/'/g, '"');

const listaInstrumentos1 = JSON.parse(json_string1);
const listaInstrumentos2 = JSON.parse(json_string2);
const listaInstrumentos3 = JSON.parse(json_string3);
const listaInstrumentos4 = JSON.parse(json_string4);
const listaInstrumentos5 = JSON.parse(json_string5);
const listaInstrumentos6 = JSON.parse(json_string6);
const listaInstrumentos7 = JSON.parse(json_string7);
const listaInstrumentos8 = JSON.parse(json_string8);
const listaInstrumentos9 = JSON.parse(json_string9);
const listaInstrumentos10 = JSON.parse(json_string10);
const listaInstrumentos11 = JSON.parse(json_string11);


// Agregar los elementos de listaInstrumentos a cancion1
listaInstrumentos1.forEach(instrumento => {
    opcionesInstrumentos.cancion1.push(instrumento);
});
listaInstrumentos2.forEach(instrumento => {
    opcionesInstrumentos.cancion2.push(instrumento);
});
listaInstrumentos3.forEach(instrumento => {
    opcionesInstrumentos.cancion3.push(instrumento);
});
listaInstrumentos4.forEach(instrumento => {
    opcionesInstrumentos.cancion4.push(instrumento);
});
listaInstrumentos5.forEach(instrumento => {
    opcionesInstrumentos.cancion5.push(instrumento);
});
listaInstrumentos6.forEach(instrumento => {
    opcionesInstrumentos.cancion6.push(instrumento);
});
listaInstrumentos7.forEach(instrumento => {
    opcionesInstrumentos.cancion7.push(instrumento);
})
listaInstrumentos8.forEach(instrumento => {
    opcionesInstrumentos.cancion8.push(instrumento);
});
listaInstrumentos9.forEach(instrumento => {
    opcionesInstrumentos.cancion9.push(instrumento);
});
listaInstrumentos10.forEach(instrumento => {
    opcionesInstrumentos.cancion10.push(instrumento);
});
listaInstrumentos11.forEach(instrumento => {
    opcionesInstrumentos.cancion11.push(instrumento);
});

console.log(opcionesInstrumentos)


const selectCanciones = document.getElementById("song_select");
const fieldsetInstrumentos = document.getElementById("instrumentOptions");

selectCanciones.addEventListener("change", () => {
    const cancionSeleccionada = selectCanciones.value;
    const instrumentos = opcionesInstrumentos[cancionSeleccionada];

// Elimina los elementos anteriores
while (fieldsetInstrumentos.firstChild) {
    fieldsetInstrumentos.removeChild(fieldsetInstrumentos.firstChild);
}

const instrumentFieldset = document.getElementById('instrumentOptions');

// Crea el elemento <legend> y asigna su contenido de texto
const legend = document.createElement('legend');
legend.textContent = 'Seleccioná tu instrumento';

// Agrega el elemento <legend> al fieldset
instrumentFieldset.appendChild(legend);

// Crea nuevos elementos para los instrumentos
instrumentos.forEach(instrumento => {
    const input = document.createElement("input");
    input.type = "radio";
    input.id = instrumento.toLowerCase();
    input.name = "instrumento";
    input.value = instrumento;

    const label = document.createElement("label");
    label.htmlFor = instrumento.toLowerCase();
    label.className = "instrumento-label";
    label.textContent = instrumento;

    fieldsetInstrumentos.appendChild(input);
    fieldsetInstrumentos.appendChild(label);
    });
});


document.addEventListener("DOMContentLoaded", function() {
    const formulario = document.getElementById("registrationForm"); // Reemplaza con el ID de tu formulario
    formulario.addEventListener("submit", function(event) {
        const cancionSeleccionada = document.getElementById("song_select").value;
        const instrumentoSeleccionado = document.querySelector('input[name="instrumento"]:checked');

        if (!cancionSeleccionada) {
            alert("Por favor, selecciona una canción.");
            event.preventDefault(); // Evita que el formulario se envíe
        } else if (!instrumentoSeleccionado) {
            alert("Por favor, selecciona un instrumento.");
            event.preventDefault(); // Evita que el formulario se envíe
        }
    });
});
