from appingresos_gastos import app, LAST_ID_FILE, MOVIMIENTOS_FILES
from flask import render_template,request,redirect
import csv
from datetime import date

@app.route("/")
def index():
    datos=[]
    fichero = open(MOVIMIENTOS_FILES,"r")
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    #recorrer el objeto csvReader y cargar cada registro en la lista datos
    for item in csvReader:
        datos.append(item) 

    fichero.close()   
    
    return render_template("index.html",data = datos)

@app.route("/new",methods=["GET","POST"])
def create():
    if request.method == "POST":
        errores = validateForm(request.form)
        if errores:
            return render_template("new.html",title="Registro",tipoAccion="Registro",tipoBoton="Guardar",error = errores,dataForm=request.form)
        else:                         
            
            #generar el nuevo id en el registro
            fichero = open(LAST_ID_FILE,"r")
            last_id = fichero.read()
            if last_id == "":
                new_id = 1
            else:
                new_id = int(last_id) + 1  
            fichero.close()
            #Guardar el nuevo last_id
            ficheroId = open(LAST_ID_FILE,"w")
            ficheroId.write(str(new_id))
            ficheroId.close()  

            #acceder al archivo y configurar para cargar nuevo registro
            mifichero = open(MOVIMIENTOS_FILES,"a",newline="")
            #llamar al metodo writer de escritura y configuramos el formato
            lectura = csv.writer(mifichero,delimiter=",",quotechar='"')
            #registramos los datos recibidos
            lectura.writerow([new_id,request.form['fecha'],request.form['concepto'],request.form['monto']])
            mifichero.close()
        return redirect("/")
    else:
        return render_template("new.html",title="Registro",tipoAccion="Registro",tipoBoton="Guardar",dataForm={})

@app.route("/update/<int:id>",methods=["GET","POST"])
def edit(id):
    if request.method == "GET": 
        mificheroUpdate = open(MOVIMIENTOS_FILES,"r")
        lectura = csv.reader(mificheroUpdate,delimiter=",",quotechar='"')
        registro_buscado=[]
        for registros in lectura:
            if registros[0] == str(id):
                #aqui en cuentro el id buscado en mi registro
                registro_buscado = registros 
        return render_template("update.html",title="Actualizar",tipoAccion="Actualización",tipoBoton="Editar",dataForm=registro_buscado)
    else:
        return f" aqui debo actualizar los datos con el registro dado id:{id}"
@app.route("/delete/<int:id>",methods=["GET","POST"])
def remove(id):

    if request.method == "GET":
        mificheroDelete = open(MOVIMIENTOS_FILES,"r")
        lectura = csv.reader(mificheroDelete,delimiter=",",quotechar='"')
        registro_buscado=[]
        for registros in lectura:
            if registros[0] == str(id):
                #aqui en cuentro el id buscado en mi registro
                registro_buscado.append(registros)        

        return render_template("delete.html",title="Eliminar", data = registro_buscado)
    else:
        #aqui seria el metodo http post
        fichero_read = open(MOVIMIENTOS_FILES,"r")        
        csvReader = csv.reader(fichero_read,delimiter=",",quotechar='"')        
        registro_buscado=[]
        for registros in csvReader:
            if registros[0] != str(id):
                #guardamos todo menos el registro con el id para borrar
                registro_buscado.append(registros)  
        fichero_read.close()

        fichero_save = open(MOVIMIENTOS_FILES,"w",newline="")
        csvWriter = csv.writer(fichero_save,delimiter=",",quotechar='"') 
        for datos in registro_buscado:
            csvWriter.writerow(datos)
        fichero_save.close()

    return redirect("/")


    
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

        
