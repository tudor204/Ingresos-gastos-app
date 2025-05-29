from appingresos_gastos import app
from flask import render_template,request
import csv

@app.route("/")
def index():
    datos=[]
    fichero = open("data/movimientos.csv","r")
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    #recorrer el objeto csvReader y cargar cada registro en la lista datos
    for item in csvReader:
        datos.append(item)    
    
    return render_template("index.html",data = datos)

@app.route("/new",methods=["GET","POST"])
def create():
    if request.method == "POST":
        #acceder al archivo y configurar para carar nuevo registro
        mifichero = open("data/movimientos.csv","a",newline="")
        #llamar al metodo writer de escritura y configuramos el formato
        lectura = csv.writer(mifichero,delimiter=",",quotechar='"')
        #registramos los datos recibidos
        lectura.writerow([request.form["fecha"],request.form["concepto"],request.form["monto"]])
        return "registro correcto"
    else:
        return render_template("new.html",title="Registro",tipoAccion="Registro",tipoBoton="Guardar")

@app.route("/update")
def edit():
    return render_template("update.html",title="Actualizar",tipoAccion="Actualizar",tipoBoton="Editar")

@app.route("/delete")
def remove():
    return render_template("delete.html",title="Eliminar",tipoAccion="Registro",tipoBoton="Guardar")
    
