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
    nombrecompleto=[]    
    ape1=[]
    ape2=[]
    hoja = abrirarchivo.sheet_by_name("Sheet1")
    for x in range(1,hoja.nrows):
        nombre.append(hoja.cell_value(x, 1).strip())
        ape1.append(hoja.cell_value(x, 2).strip())
        ape2.append(hoja.cell_value(x, 3).strip())                    
    for a in range(len(nombre)):  
        nombrecompleto.append(nombre[a]+" "+ape1[a]+" "+ape2[a])
    nombrecompleto.sort()
    os.system('cls')
    print(formatoMensaje.mensaje("Lista de personas odernada"))
    for a in range(len(nombre)): 
        print(str(a+1) +" - "+ nombrecompleto[a])
    op = menuA()
    return op