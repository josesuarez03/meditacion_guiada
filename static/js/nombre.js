document.getElementById('nameForm').addEventListener('submit', function(event){
    event.preventDefault(); // prevent form from submitting normally
    var name = document.getElementById("name").value;

    var regex_nombre = /^[a-zA-Z\s]*$/;
    if (!regex_nombre.test(name)){
        const regex_error = document.getElementById('regex');
        regex_error.innerHTML ="<p>Solo se permite caracteres y espacios.</p>";
    }

    fetch('/save-name', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({name:name})
    }).then(function(response){
        if(response.ok){
            window.location.href = '/lobby';
        } else{
            const error = document.getElementById('error');
            error.innerHTML = "<p>Error en guardar el nombre.</p>"
        }
    })
});