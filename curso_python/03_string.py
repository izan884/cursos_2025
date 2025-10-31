#string


my_string = "Mi string"
my_other_string = "Mi string"
print(len(my_string))
print(len(my_other_string))

my_new_line_string = "Esto es un string\ncon un salto de linea"
print(my_new_line_string)


my_new_line_string = "\tEsto es un stringcon tabulador"
print(my_new_line_string)

#formato
name, surname, age = "Andres", "forero", 47
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age ))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age ))

language= "Python"

language_slite = language[0:3]
print(language_slite)