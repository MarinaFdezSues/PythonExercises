# Añade las etiquetas correspondientes para su transformación a código HTML
class parseador():

    # Si es un encabezado, se coloca la cabecera
    @staticmethod
    def encabezado(txt):
        return f'<!DOCTYPE html><html lang="es-ES"><head><meta charset="utf-8"><title>{txt}</title></head><body>'

    # Si es un título, se formatea como <h2> (me parecia demasiado grande h1)
    @staticmethod
    def titulo(txt): return f'<h2>{txt}</h2>'

    # Recibe una serie de líneas de la lista, y las formatea como tal
    @staticmethod
    def listan(txt):
        l = '<ul></ul>'
        # Eliminamos los guiones y espacios que tuviera a la izquierda cada línea y se le da el formato de lista al bloque
        for elem in txt:
            nelem = elem.rstrip('\\n').replace('- ','')
            l = f'{l[:l.find("</ul>")]}<li>{nelem}</li></ul>'
        return l

    # Si es un párrafo se procesa como tal
    @staticmethod
    def procParrafo(txt): return f'<p>{txt}</p>'

    @staticmethod
    def comprobar_y_procesar_urls(texto):
        import re
        final = ''
        patron = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        # Almacenamos todas las coincidencias, si no hay, simplemente devolverá lo mismo que le entró por parámetro
        urls = re.findall(patron, texto)
        aux = texto
        # en cada vuelta almacena en la veriable final el texto y la url, pero ésta con el formato que le corresponde
        for u in urls:
            ini = aux.find(u)
            fin = ini + len(u)
            link = '<a href="' + u + '">Link</a>'
            final = final + aux[:ini] + link
            # aux va descartando el texto que ya se ha procesado
            aux = aux[fin:]
        final = final + aux
        return final

    # Devuelve las etiquetas de cierre del documento
    @staticmethod
    def cierre():
        return '</body></html>'

class reglas():
    # Función que clasifica cada línea
    @staticmethod
    def clasificacion(o):
        # inicializamos las variables que posteriormente usaremos
        titulares = []
        txtLista = []
        procLista = False
        head = ''
        texto = ''
        while o.readable():
            # Almacenamos cada línea del texto en la variable línea y quitamos los espacios iniciales y finales,
            # las tabulaciones y los saltos de linea tanto del inicio y como del final si los hubiera
            linea = o.readline().strip()
            linea = parseador.comprobar_y_procesar_urls(linea)
            # Si la 1ª línea cumple los requisitos para ser un encabezado, se formateará como uno, si no los cumple,
            # se usará 'Default'
            # La línea que se usa de cabecera también aparecerá en el cuerpo de la página
            if head == '' and len(linea) < 70 and linea.find(':') == -1: head = parseador.encabezado(linea)
            else: head = parseador.encabezado('Default')

            # Si para este bloque (procLista activo) ya no hay más líneas que añadir (empiezan por '-'),
            # se procesan los componentes de la lista almacenados en txtLista, y se resetean las variables
            if procLista and linea.find('-') == -1:
                # almacenamos en txtofinal los nuevos datos
                texto = texto + parseador.listan(txtLista)
                procLista = False
                txtLista = []

            # Si la línea EMPIEZA por '-' se considera una lista
            if linea.find('-') == 0:
                # Se van almacenando las distintas líneas de la lista en la variable auxiliar txtLista
                # y se indica que se está procesando una lista activando procLista
                txtLista.append(linea)
                procLista = True
            # Si tiene más de 70 caracteres o ':' y NO es una lista, se considera un párrafo
            elif len(linea) > 70 or linea.find(':') != -1:
                texto = texto + parseador.procParrafo(linea)
            # Si no tiene más de 70 caracteres, no es una lista, no tiene ':' y tampoco es el encabezado,
            # se considerará un título
            else:
                # 1º se almacena en la lista de títulos,
                titulares.append(linea)
                texto = texto + parseador.titulo(linea)
            # Si no hay mas lineas salimos
            if not linea:
                break
        # Por último verificamos si hay enlaces y los procesamos actualizando así la variable linea o devolviendo el
        # mismo texto, además de incluir las etiquetas iniciales y las de de cierre
        textoFinal = head + texto + parseador.cierre()
        # Cerramos el documento
        o.close()
        return textoFinal

def ejecutar():
    print('Se procederá a abrir el archivo "txtexamen.txt" y convertirá en una web llamada "examen.html"')
    textoHtml = reglas.clasificacion(abrirArchivo())
    web = crearArchivo()
    with web as f:
        f.write(textoHtml)
    print('Se ha procedido a la trasformación de su código en un documento html, puede consultarlo en el navegador, gracias.')

def crearArchivo():
    print('Se crea "examen.html". Si ya existe, se sobrescribirá.')
    return open('examen.html', 'w')

def leerCifrar(o,d):
    while o.readable():
        linea = 'cifrarLinea(o.readline())'
        print(linea)
        if not linea:
            break
    while d.readable():
        print(d.readline())
    o.close()
    d.close()

def abrirArchivo():
    try:
        return open('txtexamen.txt', 'r')
    except:
        print('Ha ocurrido un error, verifique la existencia de "txtexamen.txt" y vuelva a intentarlo.')


ejecutar()

'''

txt = 'Telefónica... https://es.wikipedia.org/wiki/Telef%C3%B3nica \n Historia\nSe fundó en Madrid el 19 de abril ... (https://cutt.ly/kj1K3P5) Marcas comerciales ...'
comprobarurls(txt)

'''