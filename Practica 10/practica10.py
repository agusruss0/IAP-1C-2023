#PRACTICA 10

#Ejercicio 1

#1.1
def contar_lineas (texto: str)->int:
    archivo = open(texto,"r")
    lineas = 0
    for _ in archivo:
        lineas +=1
    return lineas

#1.2
def existe_palabra (palabra: str, texto: str)->bool:
    archivo = open(texto, "r")
    contenido = archivo.read()
    palabras = contenido.split()
    for p in palabras:
        if palabra == p:
            return True
    archivo.close()
    return False

#1.3
def cantidad_de_apariciones(palabra: str,texto: str)->int:
    archivo = open(texto, "r")
    contenido = archivo.read()
    palabras = contenido.split()
    apariciones = 0
    for p in palabras:
        if p == palabra:
            apariciones += 1
    archivo.close()
    return apariciones

#Ejercicio 2
def clonar_sin_comentarios(texto: str)->str:
    archivo_inicial = open(texto, "r")
    archivo_nuevo = open("sincomentarios", "x")
    
    for l in archivo_inicial:
        if l.strip().startswith('#'):
            continue
        archivo_nuevo.write(l)
    archivo_inicial.close()
    archivo_nuevo.close()
    
#Ejercicio 3
def reverso (texto: str)-> str:
    archivo = open(texto, "r")
    archivo_nuevo = open("dadoVuelta.txt", "x")
    contenido = []

    for l in archivo.readlines():
        contenido.insert(0,l)
    
    archivo.close()
    print(contenido)
    
    for linea in contenido:
        archivo_nuevo.write(linea)
        
    
    archivo_nuevo.close


    



