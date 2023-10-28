async function obtenerGeneroNom(nombre){
    var api = 'https://api.genderize.io?name=' + nombre;
    try {
        const response = await fetch(api);
        const data = await response.json();
        return data.gender;
    } catch (error) {
        console.error('Error al consultar la API: ', error);
        return null;
    }
}

function saludo(){
    
}