def addLista(l,e):
	if e in l:
		raise ValueError("El elemento ya se encuentra")
	l.append(e)
	return l

lista=[1,3,5]
for i in [7,9,3]:
	try:
		print(lista, end=" + ")
		print(i, end=" = ")
		lista = addLista(lista,i)
	except ValueError as valErr:
		print(valErr)
		print("La lista se mantiene como: ", end="")
	finally:
		print(f"{lista}")
		print()
