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
    

def select_by(id):
    mificheroDelete = open(MOVIMIENTOS_FILES,"r")
    lectura = csv.reader(mificheroDelete,delimiter=",",quotechar='"')
    registro_buscado=[]
    for registros in lectura:
        if registros[0] == str(id):
            #aqui en cuentro el id buscado en mi registro
            registro_buscado.append(registros)
            
    return registro_buscado


def delete_by():
    pass
    

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
    
