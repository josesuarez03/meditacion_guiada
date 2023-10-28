# Meditacion Guiada
Este programa ayudar a los usuarios reducir sus niveles de estres con escenas relajantes y una meditación guiada.

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
