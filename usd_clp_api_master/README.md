# USD to CLP API
## Api para convertir de dolares a pesos

Antes de iniciar la api, instala las librerías con el siguiente código. Asegúrate de estar en la carpeta del proyecto.
> pip install -r requirements.txt

Para iniciar el servidor, ejecuta lo siguiente.
> python manage.py runserver

## Modo de uso

La api se usa desde la url http://127.0.0.1:8000/2

Su respuesta será
> {"clp": 1617}

En caso de querer el valor formateado, se debe agregar **?display=true** quedando http://127.0.0.1:8000/2?display=true

En este caso, su respuesta será
> {"clp": 1617, "display": "$1,617"}
