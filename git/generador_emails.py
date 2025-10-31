#Generado de emails
print('*** Generado de emails ****')

#Nombre c,ompleto del usuario
nombre_completo = ' andres hernan forero '
print(f'Nombre usurio: {nombre_completo}')
#Proceso o normalizacion el nombre del usuario
#Limpiamos los espcios en blanco al inicio y al final
nombre_normalizado = nombre_completo.strip()

nombre_normalizado = nombre_normalizado.replace(' ', '.')

nombre_normalizado = nombre_normalizado.lower()

print(f'Nombre Usuario normalizado: {nombre_normalizado}')
#Datos de la empresa
nombre_empresa = ' Global Mentoring '
print(f'\nNombre de la empresa : {nombre_empresa}')
extension_dominio = '.com.co'
print(f'Extendion del dominio: {extension_dominio}')
# qiotamos los espacios en bvlanco y convertimos a mayusculas
nombre_empresa_normalizado = nombre_empresa.replace(' ', '').lower()
dominio_email_normalizado = f'@{nombre_empresa_normalizado}{extension_dominio}'
print(f'Dominio del email bormalizado: {dominio_email_normalizado}')
#Creamos el email final
email = f'{nombre_normalizado}{dominio_email_normalizado}'
print(f'\nEmail final generado: {email}')




