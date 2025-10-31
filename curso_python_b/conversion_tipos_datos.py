# Conversion de tipos de datos

# Convertir de cadena a numero
numero_cadena = '10'
numero_entero = int(numero_cadena)

print(f"Valor numero de cadena : {numero_cadena}")
print(f"Cadena a entero : {numero_entero}")

# convertir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'Valor numero de cadena : {numero_flotante}')

#  Convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Valor numero de cadena : {numero_cadena}')
# Convertir a Booleano

# Tipo bool es falso en los siguientes casos
# Si el valor es 0, cadena vacia, o None, entonces regresa false
# Regresa verdadero, si el valor es distinto de 0, si es distinto de cadena vacia
# y tambien si es distinto de None
numero_entero = 0
booleano= bool(numero_entero)
print(f'Valor booleano de 5: {booleano}') # false, incluye 0, 0.0
cadena = ''
booleano = bool(cadena)
print(f'Valor cadena vacia : {booleano}')

cadena = 'Cadena con valor'
booleano = bool(cadena)
print(f'Valor cadena No vacia : {booleano}')

variable = None
booleano = bool(variable)
print(f'Valor variable {booleano}')