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
def reverso (texto: str) -> str:
    archivo = open(texto, "r")
    archivo_nuevo = open("dadoVuelta.txt", "x")
    contenido = []

    for l in archivo.readlines():
        contenido.insert(0,l)
    
    archivo.close()
    
    for linea in contenido:
        archivo_nuevo.write(linea)
        archivo_nuevo.write("\n")
        
    archivo_nuevo.close

#Ejercicio 4
def agregar_frase(archivo: str, frase: str) -> str:
    archivo_inicial = open(archivo, "a")
    archivo_inicial.write(frase)
    archivo_inicial.close()

#Ejercicio 5
def agregar_frase_inicio(archivo : str, frase: str) -> str:
    archivo_inicial = open(archivo, "r")
    leido = archivo_inicial.read()
    f = frase+"\n"

    archivo_inicial = open(archivo, "w")
    archivo_inicial.write(f+leido)
    
    archivo_inicial.close()

#Ejercicio 6
def promedio_estudiante(in_lu: str)->float:
    csv = open("notas.csv", "r")
    suma = 0.0
    materias = 0
    for linea in csv:
        lu , materia, fecha, nota = linea.strip().split(",") #separa primero los elmentos por comas, y luego quita el whitespace al principio y final de cada uno
    
        if lu == in_lu:
            suma += float(nota)
            materias += 1
    promedio = suma /materias
    return promedio

    




    



