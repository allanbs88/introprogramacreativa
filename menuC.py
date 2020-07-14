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
    nombrecompleto=[]    
    hoja = abrirarchivo.sheet_by_name("Sheet1")
    for x in range(1,hoja.nrows):
        nombrecompleto.append(hoja.cell_value(x, 1).strip()+" "+hoja.cell_value(x, 2).strip()+" "+hoja.cell_value(x, 3).strip())
    nombrecompleto.sort()
    os.system('cls')
    print(formatoMensaje.mensaje("Lista de personas por índice "))
    indice=int(input("Digite el índice que quiere consultar : "))
    cont=0
    for a in range(len(nombrecompleto)): 
        cont=cont+1
    if(indice > cont):
        print(formatoMensaje.mensaje("El índice sobrepasa el tamaño de la lista"))
    else:
        print('\n\n'+str(indice) +" "+ nombrecompleto[indice-1])
    op = menuA()
    return op