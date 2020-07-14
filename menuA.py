import xlrd
import os
import formatoMensaje
def menuA():    
    print("\n\na - Reimprimir\nh - Salir")
    op = str((input("Seleccione la opción ==> ")))
    return op
    
def imprimir():
    ruta = "personas.xlsx" 
    abrirarchivo = xlrd.open_workbook(ruta)
    nombre=[]
    ape1=[]
    ape2=[]
    hoja = abrirarchivo.sheet_by_name("Sheet1")
    for x in range(1,hoja.nrows):
        nombre.append(hoja.cell_value(x, 1).strip())
        ape1.append(hoja.cell_value(x, 2).strip())
        ape2.append(hoja.cell_value(x, 3).strip())                
    os.system('cls')
    print(formatoMensaje.mensaje("Lista de personas"))
    for a in range(len(nombre)):   
       print(str(a+1) + " - " + nombre[a] + " | " + ape1[a] + " | " + ape2[a])
    op = menuA()
    return op