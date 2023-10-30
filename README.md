# Meditacion Guiada
Este programa ayudar a los usuarios reducir sus niveles de estres con escenas relajantes y una meditación guiada. Utilzamos para desplegar la aplicación pythonanywhere, url: https://josesuarezb03.pythonanywhere.com/

## Caracteristicas del programa:
* Se utiliza un servidor 'Flask' para las rutas
* Tiene una ventana principal (estática) donde el usuario introduce su nombre
* Paras la escenas se utiliza el framework 'A-Frame'
* En el lobby del programa se utiliza 'Speech Synthensys' para que lea el nombre de bienvenida que contiene el nombre introducido en la vista anterior
* El lobby posee 3 escenas que cada tiene un ambiente distinto con audios diferentes y la meditación guiada

# Servidor Flask:
El servidor permite tener varias escenas que puedan ser redireccionadas, cargar el contenido multimedia, css del "index.html" y todos los recuros JS. Este tiene control de errores para cuando no se tenga acceso a algun recurso del servidor o no exista el mismo.

## Lobby:
El lobby simula una galeria de artes en la infinidad del espacio, este tiene 3 escenas que el usuario podra seleccionar

## Escenas
1. Playa: Tiene un boton para regresar al lobby, un audio e imagen que simula estar en el mar.
2. Templo Zen: Tiene un boton para regresar al lobby, un audio e imagen que simula estar en un Templo Zen.
3. Bosque: Tiene un boton para regresar al lobby, un audio e imagen que simula estar en un bosque/parque.

## Herramientas utilizadas
* Flask (python)
* Javascript
* A-frame
* API de genero, permitira tener un mensaje de bienvenida mas personalizado con respecto el nombre del usuario (proximamente)
* Speech synthesys

# Recursos

Contenidos usados usados:

 - Playa:
    - Música: https://youtu.be/nQvr0t6BU8Q?si=5wF5aHx-X0aVZz38
    - Voz: https://www.youtube.com/watch?v=pDigD65kLpE&t=4s
    - Imagen de fondo: https://pixexid.com/image/sandy-beach-nkfj1lyv

 - Templo Zen:
    - Música: https://youtu.be/1xYCqtbZwaY?si=Thb7pjtAKZXs-hOE
    - Voz: https://www.youtube.com/watch?v=pDigD65kLpE&t=4s
    - Imagen de fondo: https://pixelz.cc/images/wat-arun-buddhist-temple-bangkok-thailand-uhd-4k-wallpaper/

 - Bosque:
    - Música: https://youtu.be/Hc3VUL9rOHU?si=O92lqmGV-hvuwv0O
    - Voz: https://www.youtube.com/watch?v=pDigD65kLpE&t=4s
    - Imagen de fondo: https://dl.polyhaven.org/file/ph-assets/HDRIs/extra/Tonemapped%20JPG/golf_course_sunrise.jpg

# Agradecimientos

Muchisimas gracias a Anabel Otero que ha sido tan amable de permitirnos hacer uso de su voz dentro de este proyecto.
    Redes:
     - Instagram: https://www.instagram.com/anabel_otero/
     - Youtube: https://www.youtube.com/@AnabelOtero
