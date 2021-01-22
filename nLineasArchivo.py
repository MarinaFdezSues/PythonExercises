def nLineas(a, n):
    for i in range(0, n):
        print(a.readline().strip())
        i += 1

def crearAbrirArch():
    narchivo = f'{input("Introduzca un nombre de archivo sin extensión (si ya existe, éste se sobrescribirá): ")}.txt'
    archivo = open(narchivo, 'w')
    archivo.write('Linea 1 \nLin2Lin2\nLin ea 3 \nL i n e a 4\nl i ne a 5 .......\nSexta linea')
    return open(narchivo, 'r')

def soloAbrirArch():
    try:
        return open(f'{input("Introduzca el nombre de archivo de texto a abrir: ")}.txt', 'r')
    except:
        print('Ha ocurrido un error, intente crear o sobrescribir un nuevo archivo: ')
        return crearAbrirArch()

def nlineasArchivo():
    nlin = int(input('Introduzca el número de líneas que quiere leer'))
    opcion = input('¿Desea leer de un archivo existente? S/N (Por defecto N)').upper()
    if opcion == 'S':
        archivo = soloAbrirArch()
    else:
        archivo = crearAbrirArch()
    nLineas(archivo, nlin)
    archivo.close()

nlineasArchivo()
