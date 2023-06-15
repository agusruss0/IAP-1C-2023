from math import *
import random
import numpy as np

#PRACTICA 8

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
    if len(con)>8 and con != con.lower() and con != con.upper() and hayNum(con):
        return "VERDE"
    elif len(con)>=5:
        return "AMARILLA"
    else:
        return "ROJA"
 
def hayNum (con:str)->bool:
    for i in range(0,len(con)-1,1):
        if pertenece(con[i],"0123456789"):
            return True
    return False

print(contraSegura("caLabaz1as"))

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

#Parte 2

#Ejercicio 2

#2.1
def cambiarPoscPares(l: list[int])-> list[int]:
    for i in  range(0,len(l),2):
        l[i]=0
    return l

#2.2
def darNuevaLista (l: list[int])->list[int]:
    lista =[]
    for i in range(0,len(l),1):
        if i%2 == 0:
            lista.append(0)
        else:
            lista.append(l[i])
    return lista

#2.3
def sacarVocales (p: str)->str:
    np = ""
    for l in range(0,len(p),1):
        if p[l] not in "aeiou":
            np = np + p[l]
    return np

#2.4
def reemplazaVocales (p: str)-> str:
    res = ""
    for l in range(0,len(p),1):
        if pertenece(p[l],"aeiou"):
            res += "_"
        else:
            res += p[l]
    return res

#2.5
def daVueltaStr (p: str) ->str:
    res = ""
    for l in range(len(p)-1,-1,-1):
        res += p[l]
    return res

#Ejercicio 3

#3.1
def listaAlumno()->list[str]:
    lista = []
    while True:
        ing = input("Ingrese al alumnx: ")
        if ing == "listo":
            return lista
        else:
            lista.append(ing)

#3.2
def sube()->list[tuple]:
    res = []
    monto = 0

    while True:
        op = input("Indique operacion(C,D,X): ")
        if op == "C":
            montoIng = int(input("Indique el monto: "))
            monto += montoIng
            res.append((op,monto))
        elif op == "D":
            montoIng = int(input("Indique el monto: "))
            monto -= montoIng
            res.append((op,monto))
        else:
            return res

def sieteYMedio ()->list[float]:
    res = []
    num = random.choice([1,2,3,4,5,6,7,10,11,12])
    res.append(num)
    while True:
        turno = input("Otra carta o te plantas(C/P): ")
        if turno == "P":
            suma = 0.0
            for n in range(0,len(res)):
                if res[n]<10:
                    suma += res[n]
                elif res[n]>=10:
                    suma += 0.5
            if suma > 7.5:
                return res, "Perdiste"
            else : return res, "Ganaste"
        elif turno == "C":
            num = random.choice([1,2,3,4,5,6,7,10,11,12])
            res.append(num)

#Ejercicio 4

#4.1
def perteneceACadaUno (seq: list[list[int]], e: int)->list[bool]:
    res=[]

    for i in range(0,len(seq)):
        if pertenece(e,seq[i]):
            res.append(True)
        else : res.append(False)
    return res

#4.2 
def esMatriz (m: list[list[int]])->bool:
    for i in range(0,len(m)):
        if len(m)>0 and len(m[0])>0 and len(m[i])==len(m[0]):
            return True
        
#4.3
def filasOrdenadas (m: list[list[int]])->list[bool]:
    res = []
    if esMatriz(m):
        for i in range(0,len(m)):
            if ordenados(m[i]):
                res.append(True)
            else: res.append(False)
    return res

#4.4
def matrizElevada (d: int, p: float)-> list[list[int]]:
    m = np.random.randint((d,d))
    mALaP = [[],]
    cuenta= 1
    while cuenta<p:
        for i in range(0,len(m)):
            for j in range(0,len(m)):
                m[i][j] = m[i][j]*m[j][i]
        cuenta +=1
    return mALaP


