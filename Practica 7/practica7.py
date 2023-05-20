from math import *
#PRACTICA 6

#Ejercicio 1:

#1.1
def raizDe2 () -> float:
    return round(sqrt(2),4)

print(raizDe2())

#1.2
def imprimir_hola() -> str:
    return "Hola"

print(imprimir_hola())

#1.3

#1.4 Arme un general de factorial ya que el ej. 1.5, 1.6 y 1.7, no le veia mucho sentido a hacer varias
def factorial (x:int) -> int:
    fact = 1
    for i in range(1,x+1):
        mult = i
        fact = fact * mult
    return fact

print(factorial(2),factorial(3),factorial(4), factorial(5))

#Ejercicio 2

#2.1
def imprimir_saludo (n:str) -> str:
    return f"Hola {n}"

#nombre = input("Ingrese nombre: ")
#print(imprimir_saludo(nombre))
print(imprimir_saludo("Agus"))
      
#2.2
def raizCuadradaDe (x:int) -> float:
    if x<0:
        return "NO ESTA DEFINIDO LA RAIZ CUADRADA DE UN NRO NEGATIVO"
    else:
        return round(sqrt(x),4)
    
#numero = int(input("Ingrese numero: "))
#print(raizCuadradaDe(numero))
print(f"La raiz cuadrada de 49 = {raizCuadradaDe(49)}")

#2.3

#2.4
def esMultiploDe (n:int, m:int) -> bool:
    if m == 0:
        return "No esta definido"
    else:
        if n % m == 0:
            return True
        else: 
            return False

#n= int(input("n = "))
#m = int(input("m = "))
#print(esMultiploDe(n,m))
print(esMultiploDe(45,0)) #no esta definido
print(esMultiploDe(5,1)) #True
print(esMultiploDe(16,4)) #True
print(esMultiploDe(45,2)) #False

#2.5
def esPar (x:int) -> bool:
    if esMultiploDe(x,2):
        return True
    else:
        return False
    
#p = int(input("numero: "))
#print(esPar(p))
print(esPar(4)) #True
print(esPar(15)) #False
print(esPar(-6)) #True

#2.6
def cantidaDePizzas (comensales: int,porciones_min:int) -> int:
    porciones = comensales*porciones_min
    pizzas= ceil(porciones/8)
    return pizzas

#cantPers = int(input("Cantidad de personas: "))
#porcionesMinimas = int(input("Minima cantidad de porciones por persona: "))
#print(cantidaDePizzas(cantPers,porcionesMinimas))
print(cantidaDePizzas(5,3)) # 2
print(cantidaDePizzas(4,4)) # 2
print(cantidaDePizzas(6,3)) # 3

#Ejercicio 3

#3.1
def algunoEs0 (a:float,b:float) -> bool:
    return (a==0) or (b==0)

#a = float(input("numero 1: "))
#b = float(input("numero 2: "))
#print(algunoEs0(a,b))
print(algunoEs0(0.43,0.0)) #True
print(algunoEs0(2.0,4.0)) #False
print(algunoEs0(0.0,0.0)) #True

#3.2
def ambosSon0 (a:float,b:float) -> bool:
    return (a==0) and (b==0)

#q = float(input("numero 1: "))
#r = float(input("numero 2: "))
#print(ambosSon0(q,r))
print(ambosSon0(0.0,0.0)) #True
print(ambosSon0(0.23,5.0)) #False 
print(ambosSon0(0.4,0.0)) #False

#3.3
def esNombreLargo (nombre: str) -> bool:
    return (len(nombre)>=3) and (len(nombre)<=8)

#nom = input("nombre: ")
#print(esNombreLargo(nom))
print(esNombreLargo("Martin")) #True
print(esNombreLargo("Josefina")) #True
print(esNombreLargo("Estanislao")) #False

#3.4
def esBisiesto (año: int) -> bool:
    return (año%400==0) or ((año%4==0) and (año%100!=0))

#año = int(input("Año?"))
#print(esBisiesto(año))
print(esBisiesto(2004))
print(esBisiesto(2005))

#Ejercicio 4

#