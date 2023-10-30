async function obtenerGeneroNom(nombre){
    var api = `https://gender-api.com/get?name=${nombre}&key=kqkGxSyE6MZTuXD77CAFxrPVTfUpVcRtSwaS`;
    try {
        const response = await fetch(api);
        const data = await response.json();
        return data.gender;
    } catch (error) {
        console.error('Error al consultar la API: ', error);
        return null;
    }
}

async function saludo() {
    var msj = document.getElementById('mensaje');
    var user_name = msj.getAttribute('data-user-name');

    try {
        var genero = await obtenerGeneroNom(user_name);

        if (genero === 'male') {
            msj.setAttribute('value', 'Bienvenido ' + user_name + ', seleccione una de las escenas.');
        } 
        else if (genero === 'female') {
            msj.setAttribute('value', 'Bienvenida ' + user_name + ', seleccione una de las escenas.');
        } 
        else {
            msj.setAttribute('value', 'Bienvenido/a ' + user_name + ', seleccione una de las escenas.');
        }
    } catch (error) {
        console.error('Error al obtener el género: ', error);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    saludo();
});