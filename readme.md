# Aplicación de ingresos y gastos

Programa hecho en python con el framework flask

## Instalación
- Crear un entorno en python y ejecutar el comando:
```
pip install - r requirements.txt
```
La librería utilizada en flask: https://flask.palletsprojects.com/en/stable/

## Ejecución del programa
- inicializar el servidor de flask
- en mac: ``` export FLASK_APP=main.py``` 
- en windows:``` set FLASK_APP=main.py```

## Otra opción de ejecucion
- Crear un archivo .env y agregar lo siguiente
```FLASK_APP=main.py```
```FLASK_DEBUG=True```

y luego par lanzar en la terminal pasar el comando
```flask run```

## comando para ejecutar el servidor
``` flask --app main``` 

## Comando para ejecutar el servidor en otro puerto diferente por default es el 5000
``` flask --app main run -p 5002``` 

## Comando para ejeutar el servidor en modo debug, para realizar cambios en tiempo real 
``` flask --app main --debug run``` 