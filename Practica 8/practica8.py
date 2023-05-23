from math import *

#Ejercicio 1

#1.1 version a
def pertenece (n: int, l: list) -> bool:
    return n in l

print(pertenece(2,[1,2,3]))

#version b
def perteneceB (n: int, l: list) -> bool:
    for i in l:
        if i==n:
            return True
    return False
            
print(perteneceB(2,[3,4,5]))

#version c
def perteneceC (n: int, l:list) -> bool:
    ind = range(0,len(l),1)
    for i in ind:
        if n==l[i]:
            return True
    return False

print(perteneceC(2,[3,5,4,6,2,3,4,5]))   

#1.2
def divideATodos (s:list[int], n: int) -> bool:
    for i in s:
        if i%n!=0:
            return False
    return True

print(divideATodos([2,4,7,8],2))

#1.3
def sumaTotal (s:list[int]) -> bool:
    suma = 0
    for i in s:
        suma = suma + i
    return suma

print(sumaTotal([1,2,3]))

#1.4
def ordenados (s:list[int]) -> bool:
    i = 0
    while i < (len(s)-1):
        if s[i]>s[i+1]:
            return False
        else:
            i=i+1
    return True

print(ordenados([1,5,3]))

#1.5
def longMas7 (p: list[str]) -> bool:
    for i in p:
        if len(i)>7:
            return True
    return False

print(longMas7(["marga","papa","messi"]))

#1.6
def esPalindroma (p: str) -> bool:
    p = p.lower()
    reves = p[::-1]
    for i in range(0,len(p)-1,1):
        if p[i] != reves[i]:
            return False
    return True

print(esPalindroma("Aca"))

#1.7
def contraSegura(con: str) -> str:
    if len(con)>8 and con != con.lower() and con != con.upper():
        return "VERDE"
    elif len(con)>=5:
        return "AMARILLA"
    else:
        return "ROJA"
 
#def hayNum ()
print(contraSegura("cala"))

#1.8
def saldoActual (ls: list[tuple]) -> int:
    saldo = 0
    for i in ls:
        if i[0] == "I":
            saldo = saldo + i[1]
        else:
            saldo = saldo - i[1]
    return saldo

print(saldoActual([("I",100),("R",100),("I",500)]))

#1.9
def hayVocales (p: str) -> bool:
    cuenta = []
    for i in range(0,len(p)-1,1):
        if pertenece(p[i],"aeiou") and not pertenece(p[i],cuenta):
            cuenta.append(p[i])
        else: continue
    if len(cuenta)>=3:
        return True
    return False

print(hayVocales("mama"))