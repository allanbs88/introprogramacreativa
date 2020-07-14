import os
import xlrd
import menuA
import menuB
import menuC
import menuD
import menuE
import menuF
import formatoMensaje

 
def menu():
    os.system('cls')
    print(formatoMensaje.mensaje("Proyecto de introducción a la programación - 2020"))
    print(" a - Ver lista de personas\n b - Ordenar lista de personas\n c - Imprimir registro de lista de persona\n"
    " d - Ver lista de libros\n e - Buscar libro\n f - Prestar libro\n h - Salir")
    op = str((input("\t\nSeleccione la opción ==> ")))
    return op

#####################################################################inicio del  programa#####################################################################
opA=""
opB=""
opC=""
opD=""
opE=""
opF=""
opcion=menu()
os.system('cls')
if (opcion == "a"):
   opA = menuA.imprimir()
   while (opA != "h"):
      os.system('cls')
      opA = menuA.imprimir()    
      os.system('cls')
if (opcion == "b"):
    opB = menuB.imprimir()
    while (opB != "h"):
      os.system('cls')
      opB = menuB.imprimir()    
      os.system('cls') 

if (opcion == "c"):
    opC = menuC.imprimir()
    while (opC != "h"):
      os.system('cls')
      opC = menuC.imprimir()    
      os.system('cls')      
if (opcion == "d"):
    opD = menuD.retorno()
    while (opD != "h"):
      os.system('cls')
      opD = menuD.retorno()    
      os.system('cls')
if (opcion == "e"):
    opE = menuE.imprimir()
    while (opE != "h"):
      os.system('cls')
      opE = menuE.imprimir()    
      os.system('cls')   
if (opcion == "f"):
    opF = menuF.retorno     ()
    while (opF != "h"):
      os.system('cls')
      opF = menuF.retorno()    
      os.system('cls')      

while(opcion != "h"):
   os.system('cls')
   opcion=menu()
   
   if (opcion == "a"):
       opA = menuA.imprimir()
       while (opA != "h"):
           os.system('cls')
           opA = menuA.imprimir()    
           os.system('cls')
           
   if (opcion == "b"):
       opB = menuB.imprimir()
       while (opB != "h"):
           os.system('cls')
           opB = menuB.imprimir()    
           os.system('cls')    

   if (opcion == "c"):
       opC = menuC.imprimir()
       while (opC != "h"):
         os.system('cls')
         opC = menuC.imprimir()    
         os.system('cls')   
         
   if (opcion == "d"):
       opC = menud.retorno()
       while (opD != "h"):
         os.system('cls')
         opD = menuD.retorno()    
         os.system('cls')      

   if (opcion == "e"):
       opE = menuE.imprimir()
       while (opE != "h"):
         os.system('cls')
         opE = menuE.imprimir()    
         os.system('cls')    
   if (opcion == "f"):
       opF = menuF.imprimir()
       while (opF != "h"):
        os.system('cls')
        opF = menuF.retorno()    
        os.system('cls')            
   os.system('cls')
exit()