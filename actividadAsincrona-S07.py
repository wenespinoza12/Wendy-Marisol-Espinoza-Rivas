print("Tipos de datos")
#A continuación se presentarán los tipos de datos
print("")
#Datos de tipo Entero (Int)
print("TIPO ENTERO (int)")
#Multiplicación con 3 y una división entera con 2 variables distintas
#Multiplicación
num1 = (3)       #num1 es de tipo int
num2 = (5)       #num2 es de tipo int
num3 = (4)       #num3 es de tipo int
resultMulti = num1 * num2 * num3
#División Entera
numUn = (8)      #numUn es de tipo int
numDo = (3)      #numDo es de tipo int
resultDivEn = numUn // numDo
#Suma de variables
resultado = resultMulti + resultDivEn
print("El reultado de la suma de las variables es de: ", resultado)
print("")
#Datos de tipo Flotante (Float)
print("TIPO FLOTANTE (float)")
#Realizar exponencial con 2 y módulo 2
#Exponencial
var1 = (2.5)     #var1 es de tipo float
var2 = (4.2)     #var2 es de tipo float
resultExp = var1 ** var2
#Módulo
varUn = (1.5)    #varUn es de tipo float
varDo = (3.4)    #varDo es de tipo float
resultMod = varUn % varDo
#División de variables
#Dividir el resultado con el resultado de la suma 
resultado = resultExp / resultMod
print("El resultado de la división de las variables es de: ", resultado)
print("")
#Datos de tipo Complejo (Complex)
#Definir variables tipo Complex
print("TIPO COMPLEJO (complex)")
complej1 = 8 + 7j  #complej1 es de tipo complex
complej2 = 12 - 3j #complej2 es de tipo complex
complej3 = 3 + 6j  #complej3 es de tipo complex
complej4 = 5 - 2j  #complej4 es de tipo complex
complej = (complej1, complej2, complej3, complej4)
print("Los valores para las 4 variables de tipo complex son:", complej)
print("")
#Datos tipo Carácter (String)
#Se definirá variables por cantidad de integrantes, almacenando nombre de fruta por variable
print("TIPO CARÁCTER (string)")
inte1 = 'Papaya'  #inte1 es de tipo str
inte2 = 'Fresa'   #inte2 es de tipo str
inte3 = 'Uva'     #inte3 es de tipo str
inte4 = 'Piña'    #inte4 es de tipo str
inte5 = 'Jocote'  #inte5 es de tipo str
integrantes = (inte1, inte2, inte3, inte4, inte5)
print("Las frutas por la cantidad de integrantes son: ", integrantes)
print("")
#Datos de tipo Booleano (Bool)
#Se realizará en las estructura de control IF
print("TIPO BOOLEANO (bool)")
#A continuación se presentarán datos desde teclado
fruta = input("Ingresa el nombre de una fruta: ")
#Se utilizará estructura de control "If" para mostrar un mensaje según la fruta ingresada
if fruta == "Papaya":
    print(True, type(True))
    print("La fruta ingresada es la fruta favorita por Amanda")
if fruta == "Fresa":
    print(True, type(True))
    print("La fruta ingresada es la fruta favorita de Wendy")
if fruta == "Uva":
    print(True, type(True))
    print("La fruta ingresada es la fruta favorita de Kenia")
if fruta == "Piña":
    print(True, type(True))
    print("La fruta ingresada es la fruta favorita de Romilio")
if fruta == "Jocote":
    print(True, type(True))
    print("La fruta ingresada es la fruta favorita de Brandon")
print("")
print("La ejecución del presente programa ha finalizado")
 

