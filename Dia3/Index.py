 #los indice siempre inician en cero,
nombre="esta es una prueba"
Resultado = nombre[-5]
print(Resultado)

#para encontrar el caracter en que indice se encuentra.
nombre= "esta es una prueba"
Resultado = nombre.index("a",5,16)
print(Resultado)
#metodo Rindex
nombre= "esta es una prueba"
Resultado = nombre.rindex("a",5)
print(Resultado)

#Se puede buscar nombre completo e indica desde donde incia
# es sencible a las mayuz muetra error
#muestra error cuando buscas una letra que no es.
# una letra que esta repetida varias veces. y muestra el numero donde esta la primer resultado.
#si podemos una coma dice desde donde hasta