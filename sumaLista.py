def  sumaLista(lnums):
	suma=0
	for x in lnums:
		suma=suma+x
	return suma

lista = [1,3,8,4]
print(sumaLista(lista))

lista = [0,0,0,0]
print(sumaLista(lista))

lista = [18,32,48,56]
print(sumaLista(lista))

lista = [2,6,19]
print(sumaLista(lista))