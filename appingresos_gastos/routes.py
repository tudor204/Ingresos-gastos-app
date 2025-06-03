from appingresos_gastos import app
from flask import render_template,request,redirect
from datetime import date
from appingresos_gastos.models import select_by,select_all,delete_by,insert,update

@app.route("/")
def index():
    datos=select_all()    
    return render_template("index.html",data = datos,title="Lista")

@app.route("/new",methods=["GET","POST"])
def create():
    if request.method == "POST":
        errores = validateForm(request.form)
        if errores:
            return render_template("new.html",title="Registro",tipoAccion="Registro",tipoBoton="Guardar",error = errores,dataForm=request.form)
        else:
            insert(request.form)           
        return redirect("/")
    else:
        return render_template("new.html",title="Registro",tipoAccion="Registro",tipoBoton="Guardar",dataForm={},urlForm="/new")

@app.route("/update/<int:id>",methods=["GET","POST"])
def edit(id):
    if request.method == "GET": 
        
        registro_buscado =select_by(id,True)
        return render_template("update.html",title="Actualizar",tipoAccion="Actualización",tipoBoton="Editar",dataForm=registro_buscado,urlForm=f"/update/{id}")
    else:
        errores = validateForm(request.form)
        if errores:
            return render_template("new.html",title="Registro",tipoAccion="Registro",tipoBoton="Guardar",error = errores,dataForm=request.form)
        else:                
            registros = select_all()  
            update(registros,request.form)      
        
            return redirect("/") 

@app.route("/delete/<int:id>",methods=["GET","POST"])
def remove(id):

    if request.method == "GET":
        registro_buscado = select_by(id,True)
        return render_template("delete.html",title="Eliminar", data = registro_buscado)
    else:
        #aqui seria el metodo http post
        registro_buscado = select_by(id,False)
        delete_by(registro_buscado)      

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

        
