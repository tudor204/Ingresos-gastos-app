from appingresos_gastos import *
import csv

def select_all():
    datos=[]
    fichero = open(MOVIMIENTOS_FILES,"r")
    csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
    #recorrer el objeto csvReader y cargar cada registro en la lista datos
    for item in csvReader:
        datos.append(item) 
    fichero.close()  
    return datos    

def select_by(id, condicion):
    mificheroDelete = open(MOVIMIENTOS_FILES, "r")
    lectura = csv.reader(mificheroDelete, delimiter=",", quotechar='"')

    if condicion:
        # Buscar solo un registro específico por id
        for registros in lectura:
            if registros[0] == str(id):
                registro_buscado = registros
                registro_buscado = converterDict(registro_buscado)
                break
        else:
            registro_buscado = None
    else:
        # Devolver todos menos el registro con ese id (para eliminarlo)
        registro_buscado = []
        for registros in lectura:
            if registros[0] != str(id):
                registro_buscado.append(registros)

    mificheroDelete.close()
    return registro_buscado

def delete_by(registro_buscado):
    fichero_save = open(MOVIMIENTOS_FILES,"w",newline="")
    csvWriter = csv.writer(fichero_save,delimiter=",",quotechar='"') 
    for datos in registro_buscado:
        csvWriter.writerow(datos)
    fichero_save.close()

def insert(requestForm):
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
    lectura.writerow([new_id,requestForm['fecha'],requestForm['concepto'],requestForm['monto']])
    mifichero.close()
    
def update(registros, requestForm):
    nuevos_datos = []
    id = requestForm['id']  # Se espera que venga del campo oculto del formulario

    for fila in registros:
        if fila[0] == str(id):
            nuevos_datos.append([
                id,
                requestForm["fecha"],
                requestForm["concepto"],
                requestForm["monto"]
            ])
        else:
            nuevos_datos.append(fila)

    with open(MOVIMIENTOS_FILES, "w", newline="") as fichero:
        csvwriter = csv.writer(fichero, delimiter=",", quotechar='"')
        csvwriter.writerows(nuevos_datos)

def converterDict(registro_buscado):
    diccionario=dict()
    diccionario["id"]=registro_buscado[0]
    diccionario["fecha"]=registro_buscado[1]
    diccionario["concepto"]=registro_buscado[2]
    diccionario["monto"]=registro_buscado[3]
    return diccionario