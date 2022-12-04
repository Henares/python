#ELEMENTOS PYTHON

#LITERALES

#Los literales son los datos simples que Python es capaz de manejar:
# números: valores lógicos, enteros, decimales y complejos, en notación decimal, octal o hexadecimal
# cadenas de texto

#OPERADORES
#Los operadores son los caracteres que definen operaciones matemáticas (lógicas y aritméticas). Son los siguientes:
#  + (suma)      - (resta)       *(multiplicacion)       **(exponente)      /(division)       //(division entera)      %(modulo)      @ 
#  <<      >>      &       |       ^       ~
#  <(menor que)       >(mayor que)       <=(menor o igual que)      >=(mayor o igual que)      ==(igual que)      !=(distinto que)
# and               or              xor

#DELIMITADORES
#Los delimitadores son los caracteres que permiten delimitar, separar o representar expresiones. Son los siguientes:
# '       "       #       \
# (       )       [       ]       {       }
# ,       :       .       ;       @       =       ->
# +=      -=      *=      /=      //=     %=      @=
# &=      |=      ^=      >>=     <<=     **=

#PALABRAS RESERVADAS
# False      await      else      import     pass
# None       break      except    in         raise
# True       class      finally   is         return
# and        continue   for       lambda     try
# as         def        from      nonlocal   while
# assert     del        global    not        with
# async      elif       if        or         yield

#VARIABLES
nombre_de_la_variable = valor_de_la_variable
a, b, c = 'string', 15, True


#CONSTANTE
MI_CONSTANTE = 12

#TUPLAS
#Una tupla es una variable que permite almacenar varios datos inmutables (no pueden ser modificados una vez creados) de tipos diferentes:
mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)

print mi_tupla[1] # Salida: 15
print mi_tupla[1:4] # Devuelve: (15, 2.8, 'otro dato')
print mi_tupla[3:]  # Devuelve: ('otro dato', 25)
print mi_tupla[:2]  # Devuelve: ('cadena de texto', 15)

#LISTAS
#Una lista es similar a una tupla con la diferencia fundamental de que permite modificar los datos una vez creados:
mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]
print mi_lista[1]   # Salida: 15
print mi_lista[1:4] # Devuelve: [15, 2.8, 'otro dato']
print mi_lista[-2]  # Salida: otro dato

mi_lista[2] = 3.8 # el tercer elemento ahora es 3.8
#Las listas, a diferencia de las tuplas, permiten agregar nuevos valores:
mi_lista.append('Nuevo Dato')

#DICCIONARIOS
#Mientras que a las listas y tuplas se accede solo y únicamente por un número de índice, los diccionarios permiten utilizar una clave para declarar y acceder a un valor:
mi_diccionario = {'clave_1': valor_1, 'clave_2': valor_2, 'clave_7': valor_7} 
print mi_diccionario['clave_2'] # Salida: valor_2
#Un diccionario permite eliminar cualquier entrada:
del(mi_diccionario['clave_2'])
#Al igual que las listas, el diccionario permite modificar los valores
mi_diccionario['clave_1'] = 'Nuevo Valor'
#Un diccionario permite eliminar cualquier entrada:
del(mi_diccionario['clave_2'])
#Al igual que las listas, el diccionario permite modificar los valores
mi_diccionario['clave_1'] = 'Nuevo Valor'

#CONDICIONALES
#IF
if semaforo == verde: 
    print "Cruzar la calle"
else: 
    print "Esperar"

    if compra <= 100: 
    print "Pago en efectivo" 
elif compra > 100 and compra < 300: 
    print "Pago con tarjeta de débito" 
else: 
    print "Pago con tarjeta de crédito"


#WHILE
anio = 2001 
while anio <= 2012: 
    print "Informes del Año", str(anio) 
    anio += 1

while True:
    nombre = raw_input("Indique su nombre: ")
    if nombre:
        break

#FOR
mi_lista = ['Juan', 'Antonio', 'Pedro', 'Herminio'] 
for nombre in mi_lista: 
    print nombre

mi_tupla = ('rosa', 'verde', 'celeste', 'amarillo') 
for color in mi_tupla:
    print(color)

for anio in range(2001, 2013): 
    print "Informes del Año", str(anio)

#FUNCIONES
def mi_funcion(): 
    # aquí el algoritmo


def mi_funcion(): 
    print "Hola Mundo" 

funcion()


def funcion(): 
    return "Hola Mundo" 

frase = funcion() 
print frase


def saludar(nombre, mensaje='Hola'): 
    print mensaje, nombre 

saludar('Pepe Grillo') # Imprime: Hola Pepe Grillo

#ELEMENTOS Y CARACTERISTICAS DE LA POO

#CLASES
#El nombre de las clases se define en singular, utilizando CamelCase.
class Objeto:
    pass

class Antena:
    pass

class Pelo:
    pass

class Ojo:
    pass

#PROPIEDADES DE LA CLASE
#Las propiedades se definen de la misma forma que las variables (aplican las mismas reglas de estilo).
class Antena(): 
    color = "" 
    longitud = "" 

class Pelo(): 
    color = "" 
    textura = "" 

class Ojo(): 
    forma = "" 
    color = "" 
    tamanio = ""

class Objeto(): 
    color = "" 
    tamanio = "" 
    aspecto = "" 
    antenas = Antena() # propiedad compuesta por el objeto objeto Antena
    ojos = Ojo()       # propiedad compuesta por el objeto objeto Ojo
    pelos = Pelo()     # propiedad compuesta por el objeto objeto Pelo


#METODOS
#Los métodos son funciones
#Notar que el primer parámetro de un método, siempre debe ser self.
class Objeto(): 
    color = "verde" 
    tamanio = "grande" 
    aspecto = "feo" 
    antenas = Antena() 
    ojos = Ojo() 
    pelos = Pelo() 

    def flotar(self): 
        pass

#OBJETO
#Las clases por sí mismas, no son más que modelos que nos servirán para crear objetos en concreto.
class Objeto(): 
    color = "verde" 
    tamanio = "grande" 
    aspecto = "feo" 
    antenas = Antena() 
    ojos = Ojo() 
    pelos = Pelo() 

    def flotar(self): 
        print 12 

et = Objeto() 
print et.color 
print et.tamanio 
print et.aspecto 
et.color = "rosa" 
print et.color

#HERENCIA
#una clase que hereda de otra. Vale aclarar, que en Python, cuando una clase no hereda de ninguna otra, debe hacerse heredar de object, que es la clase principal de Python, que define un objeto.
class Antena(object): 
    color = "" 
    longitud = ""

class Pelo(object): 
    color = "" 
    textura = ""

class Ojo(object): 
    forma = "" 
    color = "" 
    tamanio = ""

class Objeto(object): 
    color = "" 
    tamanio = "" 
    aspecto = "" 
    antenas = Antena() 
    ojos = Ojo() 
    pelos = Pelo() 

    def flotar(self):
        pass

class Dedo(object): 
    longitud = "" 
    forma = "" 
    color = ""

class Pie(object): 
    forma = "" 
    color = "" 
    dedos = Dedo() 

# NuevoObjeto sí hereda de otra clase: Objeto
class NuevoObjeto(Objeto): 
    pie = Pie() 
 
    def saltar(self): 
        pass

#ACCEDIENDO A LOS METODOS Y PROPIEDADES DE UN OBJETO
#Python utiliza una sintaxis muy simple: el nombre del objeto, seguido de punto y la propiedad o método al cuál se desea acceder:
objeto = MiClase() 
print objeto.propiedad 
objeto.otra_propiedad = "Nuevo valor" 
variable = objeto.metodo()
print variable
print objeto.otro_metodo()

#METODOS DE FORMATO

#CONVERTIR PRIMERA LETRA A MAYUSCULA
#Método: capitalize()
#Retorna: una copia de la cadena con la primera letra en mayúsculas.
cadena = "bienvenido a mi aplicación" 
cadena.capitalize()
Bienvenido a mi aplicación

#CONVERTIR A MINISCULAS
#Método: lower()
#Retorna: una copia de la cadena en minúsculas.
cadena = "Hola Mundo"
print cadena.lower()
hola mundo


#CONVERTIR A MAYUSCULAS
#Método: upper()
#Retorna: una copia de la cadena en mayúsculas.
cadena = "Hola Mundo" 
print cadena.upper()
HOLA MUNDO

#CONVERTIR MAYUSCULAS A MINUSCULAS Y VICEVERSA
#Método: swapcase()
#Retorna: una copia de la cadena convertidas las mayúsculas en minúsculas y viceversa.
cadena = "Hola Mundo" 
print cadena.swapcase()
hOLA mUNDO


#CENTRAR UN TEXTO
#Método: center(longitud[, "caracter de relleno"])
#Retorna: una copia de la cadena centrada.
cadena = "bienvenido a mi aplicación".capitalize() 
print cadena.center(50, "=") 
===========Bienvenido a mi aplicación============ 

print cadena.center(50, " ") 
           Bienvenido a mi aplicación


#ALINEAR TEXTO A LA IZQUIERDA O A LA DERECHA 
#Método: ljust(longitud[, "caracter de relleno"])
#Retorna: una copia de la cadena alineada a la izquierda.
cadena = "bienvenido a mi aplicación".capitalize() 
print cadena.rjust(50, "=") 
=======================Bienvenido a mi aplicación

print cadena.rjust(50, " ") 
                       Bienvenido a mi aplicación


cadena = "bienvenido a mi aplicación".capitalize() 
print cadena.ljust(50, "=")
Bienvenido a mi aplicación=======================


#CONTAR LAS APARICIONES DE UNA SUBCADENA
#Método: count("subcadena" [, posicion_inicio, posicion_fin])
#Retorna: un entero representando la cantidad de apariciones de subcadena dentro de cadena.

cadena = "bienvenido a mi aplicación".capitalize() 
print cadena.count("a") 
3

#BUSCAR UNA SUBCADENA DENTRO DE UNA CADENA
# Método: find("subcadena" [, posicion_inicio, posicion_fin])
#Retorna: un entero representando la posición donde inicia la subcadena dentro de cadena. Si no la encuentra, retorna -1.
cadena = "bienvenido a mi aplicación".capitalize() 
print cadena.find("mi") 
13 
print cadena.find("mi", 0, 10) 
-1




# FUNCIONES INTEGRADAS
#abs()
#aiter()
#all()
#any()
#anext()
#ascii()
#bin()
#bool()
#breakpoints()
#bytearray()
#bytes()
#callable()
#chr()
#classmethod()
#compile()
#complex()
#delattr()
#dict()
#dir()
#divmod()
#enumerate()
#eval()
#exec()
#filter()
#float()
#format()
#frozenset()
#getattr()
#globals()
#hasattr()
#hash()
#help()
#hex()
#id()
#input()
#int()
#isinstance()
#issubclass()
#iter()
#len()
#list()
#locals()
#map()
#max()
#memoryview()
#min()
#next()
#object()
#oct()
#open()
#ord()
#pow()
#print()
#property()
#range()
#repr()
#reversed()
#round()
#set()
#setattr()
#slice()
#sorted()
#staticmethod()
#str()
#sum()
#super()
