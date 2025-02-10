#conversiones Explicitas
num1 = 20
num2 = 34.2
num1 = num1 +num2
print(num1)
print(type(num1))
print (type(num2))


#conversion de un float a un int
num1 = 5.8
print(num1)
print(type(num1))
num2 = int(num1)
print(num2)   #cuando se convierte de float a int quita el desimal
print(type(num2))

edad = input("cual es tu edad: ")
edad = int (edad)
nueva_edad = 1 + edad
print ("tu nueva edas es: " + str (nueva_edad))    #concatenar un Int en un STR se usa asi.
print(type(nueva_edad))

#mi primer proyecto.
peso = float (input("Cuanto pesas: "))
bajo = float (input("cuantos haz bajado: "))
print(" tu peso es de:  " + str(peso - bajo) + " Kg")

#1 practica converion a un int
num1 = 7.5
num1 = int (num1)
print(type(num1))

# conversion a un Float
num2 = 10
num2 = float (num2)
print(type(num2))

#3 conversion de float a sumarlo

num1 = 123
num2= 20.5
num1 = num1 + num2
print(type (num1))
print(type (num2))

