def subCadena(c1, c2):
	return c1.find(c2) !=-1

def alfPrimera(c1, c2):
	lista=[c1,c2]
	lista.sort()
	return lista[0]

cadena1 = 'cadena de prueba'
cadena2 = 'prueba'
cadena3 = 'otra'
print(f'¿"{cadena2}" es subcadena de "{cadena1}"? ', subCadena(cadena1, cadena2))
print()
print(f'¿"{cadena3}" es subcadena de "{cadena1}"? ', subCadena(cadena1, cadena3))
print()
print(f'Entre "{cadena2}" y "{cadena3}" la primera alfabéticamente es: ', alfPrimera(cadena2, cadena3))