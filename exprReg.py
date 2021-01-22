import re
expmail = '^[^@]+@[^@]+\.[a-zA-Z]{2,}$'
expurl = '^[(https?:\/\/]?[\w\-]+(\.[\w\-]+)+[/#?]?.[a-zA-Z]+$'

def validarMail (txt):
    if re.match(expmail,txt): print(f'"{txt}" es un e-mail válido.')
    else: print('Error, no es un e-mail válido.')
def validarUrl (txt):
    if re.match(expurl, txt): print(f'"{txt}" es una url válida.')
    else: print('Error, no es una url válida.')

validarMail(input('Introduzca un e-mail: '))
validarUrl(input('Introduzca una url: '))