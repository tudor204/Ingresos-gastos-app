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
    return render_template("new.html")
    



"""
{% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
"""