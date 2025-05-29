from appingresos_gastos import app
from flask import render_template

@app.route("/")
def index():
    datos=[
        {"fecha":"01/02/2025",
        "concepto":"Ropa",
        "monto":"-150"},
        {"fecha":"01/03/2025",
        "concepto":"Salario",
        "monto":"1500"},
        {"fecha":"15/03/2025",
        "concepto":"Supermercado",
        "monto":"-230"},
        ]
    
    return render_template("index.html",data = datos)

@app.route("/new")
def creat():
    return render_template("new.html",title="Registro",tipoAccion="Registro",tipoBoton="Guardar")

@app.route("/update")
def edit():
    return render_template("update.html",title="Actualizar",tipoAccion="Actualizar",tipoBoton="Editar")

@app.route("/delete")
def remove():
    return render_template("delete.html",title="Eliminar",tipoAccion="Registro",tipoBoton="Guardar")
    
