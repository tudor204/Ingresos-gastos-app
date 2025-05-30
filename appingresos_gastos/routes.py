from appingresos_gastos import app
from flask import render_template,request,redirect
import csv
from datetime import date

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
        errores = validateForm(request.form)
        if errores:
            return render_template("new.html",title="Registro",tipoAccion="Registro",tipoBoton="Guardar",error = errores,dataForm=request.form)
        else:              
            #acceder al archivo y configurar para carar nuevo registro
            mifichero = open("data/movimientos.csv","a",newline="")
            #llamar al metodo writer de escritura y configuramos el formato
            lectura = csv.writer(mifichero,delimiter=",",quotechar='"')
            #registramos los datos recibidos
            lectura.writerow([request.form['fecha'],request.form['concepto'],request.form['monto']])
            mifichero.close()
        return redirect("/")
    else:
        return render_template("new.html",title="Registro",tipoAccion="Registro",tipoBoton="Guardar",dataForm={})

@app.route("/update")
def edit():
    return render_template("update.html",title="Actualizar",tipoAccion="Actualizar",tipoBoton="Editar")

@app.route("/delete")
def remove():
    return render_template("delete.html",title="Eliminar",tipoAccion="Registro",tipoBoton="Guardar")
    
def validateForm(datosFormulario):
    errores=[]#lista para guardar errores
    hoy = date.today().isoformat()#capturo laf echa de hoy
    if datosFormulario["fecha"] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datosFormulario["concepto"] =="":
        errores.append("El concepto no puede ir vacío")
    if datosFormulario["monto"] =="" or float(datosFormulario["monto"]) == 0.0:
        errores.append("El precio debe ser distinto a 0 y de vacío")
    return errores

        
