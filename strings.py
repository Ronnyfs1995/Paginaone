myStr = "Ronny"

#metodo para concatenar valores de la variable e imprimir por pantalla 

print("My name is " + myStr)
print(f"My name is {myStr}")
print("My name is {0}".format(myStr))


# print(dir(myStr))

print(myStr.upper())  #metodo de mayúsculas para variable
print(myStr.lower()) #metodo de minúsculas para variable
print(myStr.swapcase()) #metodo de mayusculas 
print(myStr.capitalize()) #metodo para mayusculas en iniciales unicamente
print(myStr.replace('hello', 'bye')) #metodo para reemplazar palabras
print(myStr.count('l')) #metodo para contar letras 

print(myStr.startswith('hola')) #metodo para consultar con que palabra empieza el texto de la variable

print(myStr.endswith('world')) #metodo para consultar con que palabra termina el texto de la variable


#metodo para separar las palabras de la variable 

print(myStr.split()) 

print(myStr.split(',')) #tomando la coma

#metodo para buscar posición de una letra
print(myStr.find('o'))

print(len(myStr)) #metodo para contar la cantidad de letras de la variable

print(myStr.index('e')) #metodo para conocer el indice de la letra

print(myStr.isnumeric()) #metodo para conocer si el valor de la variable es numérica
print(myStr.isalpha()) #metodo para conocer si el valor de la variable es alfanumérica

# print(myStr[3]) #metodo para mostrar el caracter en la posición que se indica
# print(myStr[-1]) #De atrás para adelante









