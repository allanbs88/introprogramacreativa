import xlrd
import os
import formatoMensaje
salida=""
def menuA():    
    print("\n\na - Volver a buscar\nh - Salir")
    op = str((input("Seleccione la opción ==> ")))
    return op

def imprimir():
    ruta = "libros.xlsx" 
    abrirarchivo = xlrd.open_workbook(ruta)
    dicLibro = {}
    hoja = abrirarchivo.sheet_by_name("Hoja1")
    item=hoja.nrows
    for x in range(1,hoja.nrows):
        dicLibro["id"+str(x)] = int(hoja.cell_value(x, 0))
        dicLibro["nombre"+str(x)] = str(hoja.cell_value(x, 1)).strip()
        dicLibro["genero"+str(x)] = hoja.cell_value(x, 2).strip()
        dicLibro["autor"+str(x)] = hoja.cell_value(x, 3).strip()
    nombre = input("Digite el nombre que quiere buscar: ")

    u=1
    while (u<item):
        enc = dicLibro["nombre"+str(u)].find(nombre)
        if(enc >= 0):
            print(formatoMensaje.mensaje("Libro encontrado"))  
            print(formatoMensaje.mensaje("ID --- Nombre --- Genero --- Autor")) 
            print(str(dicLibro["id"+str(u)]) + " - " + str(dicLibro["nombre"+str(u)]) + " | " + dicLibro["genero"+str(u)] + " | " + dicLibro["autor"+str(u)])
            break
        u=u+1
    op = menuA()
    return op
    
    