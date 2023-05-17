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

#1.3 Arme un general de factorial ya que el ej. 1.5, 1.6 y 1.7, no le veia mucho sentido a hacer varias
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
print(esMultiploDe(45,0)) #no esta definido)
print(esMultiploDe(5,1)) #True
print(esMultiploDe(16,4)) #True
print(esMultiploDe(45,2)) #False