#Esto es un comentario de una sola linea
"""
ESTO ES UN COMENTARIO DE
VARIAS LINEAS
"""

print("Hola Mundo")
x = 10
print(type(x))
print(x)
x = y = z = 2.3
print(x , y , z)
print(type(x))
x = "cadena"
print(type(x))

#Concatenando cadenas
c1 = "Hola"
c2 = "Eduardo"
saludo  = c1 +" "+c2
print(saludo)

#Agrega un numero al final del mensaje
saludo2 = "{} {} {}".format(c1, c2 , 3)
print(saludo2)

#Cambia el orden en que es impreso el mensaje en terminal
saludo3 = "Cambio de orden {1} {2} {0}".format(c1 , c2 , 3)
print(saludo3)