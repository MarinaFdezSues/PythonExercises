def mostrarVal(d,k):
	if d.get(k) == None:
		raise ValueError(f'La clave {k} no se encuentra en el diccionario')
	return (d[k])

dicc = {1:'a', 3:'c',5:'f'}
for i in [3, 7, 5]:
	try:
		print( f'Clave: {i}, valor: {mostrarVal(dicc,i)}' )
	except ValueError as valErr:
		print(valErr)
	finally:
		print()