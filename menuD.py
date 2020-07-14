import xlrd
import os
import formatoMensaje
def menuA():    
    print("\n\na - Reimprimir\nh - Salir")
    op = str((input("Seleccione la opción ==> ")))
    return op

def cargar():
    ruta = "libros.xlsx" 
    abrirarchivo = xlrd.open_workbook(ruta)
    dicLibro = {}
    hoja = abrirarchivo.sheet_by_name("Hoja1")
    item=hoja.nrows
    for x in range(hoja.nrows):
        dicLibro["id"+str(x)] = hoja.cell_value(x, 0)
        dicLibro["nombre"+str(x)] = hoja.cell_value(x, 1)
        dicLibro["genero"+str(x)] = hoja.cell_value(x, 2).strip()
        dicLibro["autor"+str(x)] = hoja.cell_value(x, 3).strip()
    salida=""
    print(formatoMensaje.mensaje("Lista de Libros"))  
    print(formatoMensaje.mensaje("ID --- Nombre --- Genero --- Autor"))        
    u=1
    while(u<item):
        salida = salida + str(dicLibro["id"+str(u)]) + " - " + str(dicLibro["nombre"+str(u)]) + " | " + dicLibro["genero"+str(u)] + " | " + dicLibro["autor"+str(u)] + "\n"
        u=u+1 
    return salida

def retorno():
    print(cargar())  
    op = menuA()
    return op
