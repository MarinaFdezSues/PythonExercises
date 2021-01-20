def dosPrimCarac(c):
	return c[:2]

def tresUltCarac(c):
	return c[len(c)-3:]

def cadenaCadaDosCarac1(c):
	i = 0
	txt = ''
	while i < len(c):
		txt += c[i:]+'\n'
		i += 2
	return txt.strip()

def cadenaCadaDosCarac2(c):
	i = 0
	txt = ''
	while i < len(c):
		txt += c[i]
		i += 2
	return txt.strip()

def cadenaInvertida(c):
	return c[::-1]

cadena = 'cadena de prueba'
print('Dos primeros caracteres de la cadena:')
print(dosPrimCarac(cadena))
print()
print('Tres últimos caracteres de la cadena')
print(tresUltCarac(cadena))
print()
print('Cadena cada 2 caracteres:')
print('-> Si supongo que se devuelve toda la cadena cada dos caracteres')
print(cadenaCadaDosCarac1(cadena))
print()
print('-> Si supongo que devuelvo una cadena con los caracteres pares')
print(cadenaCadaDosCarac2(cadena))
print()
print('Cadena invertida:')
print(cadenaInvertida(cadena))