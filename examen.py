class parseador():
    doc = '<!DOCTYPE html><html><body></body></html>'
    titulares = []

    def encabezado(self, txt):
        return f'{self.doc[:self.doc.find("</head>")]}<head><title>{txt}</title></head>{self.doc[self.doc.find("</head>"):]}'

    def titulo(self, txt):
        self.titulares.append(txt)
        return f'<h1>{txt}</h1>'

    def lista(txt):
        l = '<ol></ol>'
        for elem in txt:
            l = f'{l[:l.find("</ol>")]}<li>{elem}</li></ol>'
        return l


class reglas():
    def __init__(self):
        return self
