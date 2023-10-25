function leerMensaje(){
    var mensaje = document.getElementById('mensaje');
    if (mensaje){
        var texto = mensaje.getAttribute('value');

        if ('speechSynthesis' in window) {
            var synthesis = window.speechSynthesis;

            var mensajeVoz = new SpeechSynthesisUtterance(texto);

            synthesis.speak(mensajeVoz);
        } else {
            alert('Tu navegador no admite síntesis de voz.');
        }
    }
}

window.addEventListener('load', leerMensaje);