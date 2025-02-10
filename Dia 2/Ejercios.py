num1 = 28  #tipo de dato int
num2 = 30.1 # tipo de dato Float


num1 = num1 + num2
print(num1)
print(type (num1))
print(type (num2))

nun3 = 5.8
print(nun3)
print(type (nun3))

nun4 = int (nun3)
print(nun4)
print(type (nun4))

edad = input("dime tu edad ")
print(type (edad))
edad = int (edad)


nueva_edad = 10 + edad
print(type (nueva_edad))
print("Esta es tu nueva edad " + str (nueva_edad))

#Funcion format
nombre = "yaneth"
print("hola {}. tienes {} mensajes nuevos" .format(nombre,10))
#funcion Formar
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print("Estimado/a {}, su número de asociado es: {}".format(nombre_asociado,numero_asociado))

X= 10
Y= 35
print("La suma de es  " + str (X - Y))
print(f"la suma de {X} y {Y} es igual a {X*Y}")
print("la suma de {} y de {} es igual a {}".format(X,Y,X/Y))

#Ejercisio de redondeo
print (round(10/3,2))