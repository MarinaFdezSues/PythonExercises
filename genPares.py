def genPares():
	n=1
	while(True):
		yield n*2

pares = genPares()
print(next(pares))
print(next(pares))
print(next(pares))
print(next(pares))