#Comentario de una linea

""" 
    
    Comentarios multilinea
    
    Que es una variable: Es un espacio de memoria reservado. que puede
    cambiar en el transcurso del programa.
    
    Es un lenguaje de tipo dinamico: que no es necesario declarar
    explicitamente el tipo de variable antes de usarla.
    El tipo de dato se infiere segun el valor
    
"""
    
entero = 5
#Para imprimir dato de python se utiliza la funcion print
print(entero)
#Para saber el tipo de dato de una variable type()
print(type[entero])
    
#Para declarar variable de python: se utilizan letras, numeros, guionbajo
#Debe comenzar por una letra
#Case sensitive
variableUno = 1
variableuno = 2

"""
Palabras reservadas en Python:
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif,
else, except, finally, for, global, if, inport, in, is, lambda, nonLocal, not, or, pass,
raise, return, try, while, whith y yield.   
"""

#Tipos de datos de python

verEntero = 2
flotante = 1,75
booleanoTrue = True
booleanoFalse = False
cadenaTexto = "Soy una cadena de texto"

suma = 4+10
resta = 10-4
divicion = 10/2
multiplicacion = 6*6 


print(suma)
print(resta)
print(divicion)
print(multiplicacion)

#Concatetacion de cadenas
saludo = " hola"
nombreAlumno = " Pedro"
mensaje = saludo + nombreAlumno + " Como estas"
print(mensaje)


edad = 18
es_estudiante = True
tiene_trabajo = False
# Operaciones logicas con booleanos
es_mayor_de_edad = edad >= 18 #comprobamos si la edad es mayor o igual a
18
puede_votar = es_mayor_de_edad and tiene_trabajo


print("es mayor de edad? ", es_mayor_de_edad)
print("Puede volar? v", puede_votar)


#Listas: son colecciones de dator ordenados y modificiados.
#Pueden contener distintos tipos de datos. Para declarar una lista utilizamos corchetes ]]

numeros = [1,2,3,4,5,6,7,8,9] #Lista de numero
alumno = ["Juan","Alberto","Fulanito"]#lista de cadenas
listaMixta = [1,"Hola",False, 1.2] #Lista mixta

print(listaMixta) #Lista completa
print(listaMixta[2])#Lista detallada
print(listaMixta[-2])#Orden inverso las listas parten desde el numero 1

#tuplas: son colecciones de datos ordemas e inmutable. Una vez han sido creadas no se pueden modificar los datos. ()

coordenadas = (10,20)
meses = ("Enero","Febrero","Marzo")

print(meses[0])
print(meses[1])


#conjuntos: son colecciones de datos desordenados y no indexados.
#Se pueden definir de dos maneras 1 - {} 2 - ()

numerosPrimos = {2,3,5,7,11}
lenguaje = set("Python3")
#Agregar elementos a un conjunto
numerosPrimos.add(13)
lenguaje.remove("3")

print(numerosPrimos)
print(lenguaje)

#Diccionarios de datos: Son colecciones de datos desordenados creados mediante una clave y valor {}


persona = {
    "Nombre": "Marcelo",
    "Nacionalidad": "Chileno de corazon",
    "Ciudad": "Puerto Montt",
}
print(persona["Nombre"])#Imprimir un diccionario con un dato especifico
#Modifica un dato especifico
persona["Nacionalidad"] = "Chileno"
print(persona)
#Agrega nuevos datos al diccionario clave]: valor
persona["edad"] = 190
print(persona)


curso = 10

curso = 20
print(curso)

#Cambiar el tipo de dato

numero1= int (input("Ingrese un numero"))
numero2= int (input("Ingrese un numero"))
suma = numero1 + numero2
print(suma)
print(type(numero1))


"""
ejercicio 1 convertir temperatura de farenheit a celcius

ejercicio 2 calcular la edad exacta del usuario y consultar al usuario  si ya estuvo e cumple este 
año o no.

"""
#Ejercicio 1
farenheit = int(input("Ingrese la temperatura farenheit"))
celcius = (farenheit -32)/ 1.8
print(celcius)

#Ejercicio 2
año = int (input("ingresa tu año de nacimiento"))
añoActual = int (input("Ingresa, el año actual"))

edad = añoActual - año
print("En este año {} tienes {}".format(año, edad)) 








def suma():
    numeroUno = int(input("Escribe el primero numero a sumar "))
    numeroDos = int(input("Escribe el segundo numeroa sumar "))
    resultado=numeroUno+numeroDos
    print(resultado)



def resta():
    num1 = int(input("Escriba el primer numero a restar "))
    num2 = int(input("Escriba el segundo numero a restar "))
    resultado=num1-num2
    print(resultado)



def multiplicacion():
    num1 = int(input("Escriba el primer numero a multiplicar "))
    num2 = int(input("Escriba el segundo numero a multiplicar "))
    resultado=num1*num2
    print(resultado)


def divicion():

    num1 = int(input("Escriba el primer numero a dividir "))
    num2 = int(input("Escriba el segundo numero a dividir "))
    resultado=num1/num2
    print(resultado)


print ("Opciones: 1 sumar) 2 restar) 3 multiplicar) 4 dividir ")
opciones = int(input("Eligue una opcion "))
if opciones == 1:
        suma()
if opciones == 2:
        resta()
if opciones == 3:
        multiplicacion()
if opciones == 4:
        divicion()


