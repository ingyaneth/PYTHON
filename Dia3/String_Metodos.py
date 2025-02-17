#utilizaremos los 6 metodos mas importantes en lenguaje Pytohn
#1: Upper = pasar a mayuscula "2:Lower = pasar a minuscula. 3:Split=Seprarlo en partes.
#4:Join= unirt items usand separador. 5:find= encontrar un Sub_string 6:Replace=Reemplazar un sub_string.

texto = "este es un texto para los metodos de String"

resultado = texto [2].upper()
print(resultado)


texto = "este es un texto para los metodos de String"

resultado = texto .lower()
print(resultado)

#split separar en lista
texto = "este es un texto para los metodos de String"

resultado = texto .split()
print(resultado)

#Join 'Unir itenes separados'
a = "Aprender"
b = "Python"
c = "Es muy"
d = "Genial y facil de aprender"
e = "_" .join([a, b ,c ,d ])
print(e)

# find encontrar un sub-String
texto = "este es un texto para los metodos de String"
resultado = texto.find("")
print(resultado)

# replace= para reemplazar una texto por otro
texto = "este es un texto para los metodos de String"
resultado = texto.replace("un texto" , "una prueba")
print(resultado)

#ejercicio 2 de metodos de String
lista_palabras = ["La","legibilidad","cuenta."]
resultado= " ".join (lista_palabras)
print(resultado)


#ejercio #3 de la case de metodos dce string
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado =frase.replace ("difícil","facil")
resultado =resultado.replace ("mala","buena")
print(resultado)
#otra manera de resolver.
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado =frase.replace ("difícil","fácil") .replace ("mala","buena")
print(resultado)