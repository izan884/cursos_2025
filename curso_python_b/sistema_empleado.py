print('*** Sistema de Empleados ***')
nombre_empleado = input('Nombre empleado: ')
edad_empleado= int(input('Edad: '))
salario_empleado = float(input('Salario: '))
es_jefe_de_departameto = input('Es jefe departamento (Si/No)?')

es_jefe_de_departameto = es_jefe_de_departameto.lower() == 'si'

# Imprimir los valores del Empleado
print(f'\nDatos del Empleado')
print(f'Nombre empleado: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}')
print(f'Es jefe: {es_jefe_de_departameto}')

