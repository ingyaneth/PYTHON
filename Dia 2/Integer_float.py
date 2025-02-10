# utilizamos la funcion Type para saber que tipo numerico es
#INT se utiliza par numero enteros negtivos o positivos

#Funcion Type para saber que tipo de dato estamos trabajando ('int')
mi_numero = 7
print(mi_numero + mi_numero)
print (type(mi_numero))

# funcion Type para tipo de dato (Float)
mi_peso = 99.5 + mi_numero
print(mi_peso + int (mi_numero))
print(type(mi_peso))

# cuando es un String (cadena) tambien podemos utilizar Type
mi_aniversario = "septiembre "
print(mi_aniversario + str (mi_numero))
print(type(mi_aniversario))


edad = input("dime tu edad: ")
print("tu edad es " + edad + ' años')

#ejercicio 1 int
num_entero = 7
print (type(num_entero))

#2ejercisio Float
num_decimal = 85.4
print (type (num_decimal))

# 3 ejercisio variables pero que imprima el tipo de dato.
num1 = 7.5
num2 = 2.5
print (type(num1 + num2))