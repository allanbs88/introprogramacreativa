import xlrd
import os
import json
from datetime import datetime
def opciones():
	print("Opciones 1: Imprimir personas")
	print("Opciones 2: Imprimir libros")
	print("Opciones 3: Prestar")
	print("Opciones 4: Imprimir prestamos")
	print("Opciones 5: Salir")
    
def ListaLibros():
    ruta = "libros.xlsx" 
    abrirarchivo = xlrd.open_workbook(ruta)
    dicLibro = {}
    hoja = abrirarchivo.sheet_by_name("Hoja1")
    item=hoja.nrows
    dicLibro["libro"] = []
    for x in range(1,item):
        dicLibro["libro"].append({"id":int(hoja.cell_value(x, 0)),"nombre":hoja.cell_value(x, 1),"genero":hoja.cell_value(x, 2),"autor":hoja.cell_value(x, 3)})

    with open('libros.txt', 'w') as outfile:
        json.dump(dicLibro, outfile, indent=3)

    with open('libros.txt') as json_file:
        data = json.load(json_file)
        print('Lista de Libros')
        for p in data["libro"]:
            print('ID    : ' + str(p["id"]))
            print('Nombre: ' + str(p["nombre"]))
            print('Genero: ' + p["genero"])
            print('Autor : ' + p["autor"])        
            print('')
            
def ListaPersonas():            
    ruta = "personas.xlsx" 
    abrirarchivo = xlrd.open_workbook(ruta)
    dicPersona = {}
    hoja = abrirarchivo.sheet_by_name("Sheet1")
    item=hoja.nrows
    dicPersona["persona"] = []
    for x in range(1,item):
        dicPersona["persona"].append({"id":int(hoja.cell_value(x, 0)),"nombre":hoja.cell_value(x, 1).strip(),"primerap":hoja.cell_value(x, 2).strip(),"segundoap":hoja.cell_value(x, 3).strip(),"correo":hoja.cell_value(x, 4).strip()})
    with open('personas.txt', 'w') as outfile:
        json.dump(dicPersona, outfile, indent=3)
    with open('personas.txt') as json_file:
        data = json.load(json_file)
        print('Lista de Personas')
        for p in data["persona"]:
            print('ID        : ' + str(p["id"]))
            print('Nombre    : ' + p["nombre"])
            print('Apellido1 : ' + p["primerap"])
            print('Apellido2 : ' + p["segundoap"])
            print('Correo    : ' + str(p["correo"]))           
            print('')

def retorno():
    ejecuta = True
    prestamo = []
    while (ejecuta):

        opciones()
        opcion = int(input("Seleccione la opción ==> "))
        os.system('cls')

        if(opcion == 1):
            ListaPersonas()


        if(opcion == 2):
            ListaLibros()

        if(opcion == 3):
            print("")
            ListaPersonas()
            idPersona = int(input("Seleccione la cédula de la persona : "))
            os.system('cls')
            print("")
            ListaLibros()
            idLibro = int(input("Seleccione el ID de un libro       : "))
            os.system('cls')
            prestamoTMP = {}
            prestamoTMP["idPersona"] = idPersona
            prestamoTMP["idLibro"] = idLibro
            prestamoTMP["fecha"] = datetime.now()

        if(opcion == 4):
            os.system('cls')
            print('Detalle de préstamo\n')
            
            print('Cédula  : ' + str(prestamoTMP["idPersona"]))
            print('Libro   : ' + str(prestamoTMP["idLibro"]))
            print('Fecha   : ' + str(prestamoTMP["fecha"])) 
        if(opcion == 5):
            ejecuta = False
            return 'h'    