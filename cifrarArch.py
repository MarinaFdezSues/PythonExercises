#Implementar una función que reciba un archivo de texto de origen y uno de destino,
#de modo que para cada línea del archivo origen,
#se guarde una línea cifrada en el archivo destino.
#El algoritmo de cifrado a utilizar consiste en lo siguiente:
#cada carácter comprendido entre la a y la z, se le suma 13
#y luego se aplica el módulo 26, para obtener un nuevo carácter.

abc = 'zabcdefghijklmnñopqrstuvwxy'
def cifrarLinea(linea):
	cifrado = ''
	for i in linea:
		cifrado = cifrado + cifrarC(i)
	return cifrado

def cifrarC (c): 
	if abc.find(c) == -1 : return c
	else: return abc[(abc.find(c) + 13) % 26]
		#return caracter((pos(c) + 13) % 26)
#def pos(caracter): return abc.find(c)
#def caracter(pos): return abc[pos]



print(cifrarLinea('abcde.fghijklm nño?pqrstuvw@xyz'))
print('de momento el cifrado está')