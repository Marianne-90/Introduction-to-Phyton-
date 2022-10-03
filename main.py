from Empleado import Empleado
from Cliente import Cliente



def cargar():
  respuesta = input('¿Vas a agregar un empleado? ')
  nombre= input('Ingresa Nombre ')
  apellido = input('Ingresa el apelldido ')
  dni = input('Ingresa el dni ')
  telefono = input('Ingresa el telefono ')

  if (respuesta == 'si'):
    salario = input('Ingresa el salario ')
    emp = Empleado(nombre, apellido, dni, telefono, int(salario))
    personas.append(emp)
  else:
      categoria = input('Ingresa la categoría')
      cli = Cliente( nombre, apellido, dni, telefono, categoria)
      personas.append(cli)

  
personas = []
cargar()
cargar()
for persona in personas:
  print(persona)