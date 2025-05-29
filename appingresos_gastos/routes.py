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
def creat():
    if request.method == "POST":
      
        return f"datos a registar:{request.form}"

    return render_template("new.html",title="Registro",tipoAccion="Registro",tipoBoton="Guardar")

@app.route("/update")
def edit():
    return render_template("update.html",title="Actualizar",tipoAccion="Actualizar",tipoBoton="Editar")

@app.route("/delete")
def remove():
    return render_template("delete.html",title="Eliminar",tipoAccion="Registro",tipoBoton="Guardar")
    
