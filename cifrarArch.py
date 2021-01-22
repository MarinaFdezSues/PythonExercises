# Implementar una función que reciba un archivo de texto de origen y uno de destino,
# de modo que para cada línea del archivo origen,
# se guarde una línea cifrada en el archivo destino.
# El algoritmo de cifrado a utilizar consiste en lo siguiente:
# cada carácter comprendido entre la a y la z, se le suma 13
# y luego se aplica el módulo 26, para obtener un nuevo carácter.
def cifrarLinea(linea):
    cifrado = ''
    for i in linea:
        cifrado = cifrado + cifrarC(i)
    return cifrado
def cifrarC(c):
    abc = 'zabcdefghijklmnñopqrstuvwxy'
    if abc.find(c) == -1:
        return c
    else:
        return abc[(abc.find(c) + 13) % 26]
def abrirArchivo2():
    print("Se escribirá el contenido cifrado en el archivo CIFRADO.txt. Si ya existe, se sobrescribirá.")
    return open('CIFRADO.txt', 'w')
def abrirArchivo1():
    try:
        return open(f'{input("Introduzca el nombre del archivo de texto a leer: ")}.txt', 'r')
    except:
        print('Ha ocurrido un error, intentelo de nuevo: ')
        return abrirArchivo1()
def leerCifrar(o,d):
    while o.readable():
        linea = cifrarLinea(o.readline())
        print(linea)
        if not linea:
            break
    while d.readable():
        print(d.readline())
    o.close()
    d.close()

leerCifrar(abrirArchivo1(),abrirArchivo2())
