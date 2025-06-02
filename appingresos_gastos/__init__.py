from flask import Flask

app = Flask(__name__)
MOVIMIENTOS_FILES = "data/movimientos.csv"
LAST_ID_FILE = "data/last_id.csv"

from appingresos_gastos.routes import *

#inicializar el servidor de flask
#en mac: export FLASK_APP=main.py
#en windows: set FLASK_APP=main.py

#Comando para ejeutar el servidor en modo debug, para realizar cambios en tiempo real 
#flask --app main --debug run
