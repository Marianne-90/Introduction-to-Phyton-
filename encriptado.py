def encriptar(texto):
  textoFinal=''
  for letra in texto:
    ascii= ord(letra)
    ascii += 1 
    textoFinal += chr(ascii)
  return textoFinal
    
def desencriptar(texto):
    contador=0
    textoFinal=''
    for letra in texto:
      ascii= ord(letra)
      ascii -= 1 
      textoFinal += chr(ascii)
    return textoFinal



def encriptarArchivo(rutaArchivo):
  archivo = open(rutaArchivo, 'r')
  texto = archivo.read()
  archivo.close()
  textoEncriptado =  encriptar(texto)
  
  archivo = open(rutaArchivo, 'w')
  archivo.write(textoEncriptado)
  archivo.close()
  print('encriptado completado')


def desEncriptarArchivo(rutaArchivo):
  archivo = open(rutaArchivo, 'r')
  texto = archivo.read()
  archivo.close()
  textoDesncriptado =  desencriptar(texto)
  
  archivo = open(rutaArchivo, 'w')
  archivo.write(textoDesncriptado)
  archivo.close()
  print('desencriptado completado')
respuestaEoD = input('Presiona "E" para encriptar, o "D" para desencriptar ')

rutaArchivo = input('ingrese la ruta del archivo ')

if respuestaEoD == 'E':
  encriptarArchivo(rutaArchivo)
if respuestaEoD == 'D':
  desEncriptarArchivo(rutaArchivo)