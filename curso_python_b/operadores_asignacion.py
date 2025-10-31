print('*** Operadores de Asignacion ***')
numero = 5
print(f'Valor de numero: {numero} ')
numero = 10
print(f'Valor de numero: {numero} ')
cadena = 'Saludos desde Python'
print(f'cadena : {cadena} ')

#asignacion Multiple
x, y , z = 5, 'Hola', -9.15
print(f'x : {x} y : {y} z : {z}')

# asignacion encadenada.
a = b = c = 10
print(f'a : {a} b : {b} c : {c}')

# Recibir multiples valores de entrada del suaurio
nombre, apellido = input('Ingresa tu nombre y apelldo separado por coma: ').split(',')
print(f'Nombre: {nombre.strip()} apellido: {apellido.strip()}')



