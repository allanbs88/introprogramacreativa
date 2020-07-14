def mensaje(mensaje):
  salida=""  
  if (mensaje != ""):
    salida = "╔"
    #no entiendo por que la *
    #cols = (len(mensaje) * 5) + len(mensaje)-1
    cols = (len(mensaje)+2)
    for f in range(cols):
      salida = salida + "═"
    
    salida= salida + "╗"

    salida = salida + '\n' + "║ " + mensaje
    for f in range(cols - len(mensaje) - 1):
      salida = salida + " "
    salida = salida + "║"

    salida = salida + '\n' + "╚"
    for f in range(cols):
      salida = salida + "═"
    salida = salida + "╝"
  return salida