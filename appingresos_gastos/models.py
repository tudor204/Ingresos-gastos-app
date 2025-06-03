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
    

def select_by(id,condicion):
    mificheroDelete = open(MOVIMIENTOS_FILES,"r")
    lectura = csv.reader(mificheroDelete,delimiter=",",quotechar='"')
    registro_buscado=any
    for registros in lectura:
        if condicion == True:
            if registros[0] == str(id):
                #aqui en cuentro el id buscado en mi registro
                registro_buscado = registros

        else:
            if registros[0] != str(id):
                #guardamos todo menos el registro con el id para borrar
                registro_buscado.append(registros)

    if condicion == True:
        registro_buscado = converterDict(registro_buscado)

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
    
def update(registros,requestForm):
    lista=[]
    for key,value in registros:
        lista.append(value)

    nuevos_datos=[]
    
    for item in registros:           
        if value == str(id):
            nuevos_datos.append([id,requestForm["fecha"],requestForm["concepto"],requestForm["monto"]])
        else:
            nuevos_datos.append(value)
                
        fichero = open(MOVIMIENTOS_FILES,"w",newline="")
        csvwriter = csv.writer(fichero,delimiter=",",quotechar='"')
        csvwriter.writerows(nuevos_datos)

def converterDict(registro_buscado):
    diccionario=dict()
    diccionario["id"]=registro_buscado[0]
    diccionario["fecha"]=registro_buscado[1]
    diccionario["concepto"]=registro_buscado[2]
    diccionario["monto"]=registro_buscado[3]