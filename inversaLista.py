def  inversaLista(l1):
	l2=[]
	for x in l1:
		l2.insert(0,x)

	print("Inicial: ", l1[:])
	print("Final: ", l2[:])
	

def  inversaLista2(l1):
	l2=[]
	for x in l1:
		laux=[]
		laux.append(x)
		laux.extend(l2)
		l2=[]
		l2.extend(laux)

	text="Inicial: ["
	strl = ",".join(map(str, l1))
	text=text+strl+"]"
	text=text + "\n"

	
	text=text + "Final: ["
	strl = ",".join(map(str, l2))
	text=text+strl+"]"
	
	return text

inversaLista([1,3,8,4])

print() 

inversaLista(["gato","perro","conejo"])

print() 

lista = [1,3,8,4]
print(inversaLista2(lista))

print() 

lista = ["gato","perro","conejo"]
print(inversaLista2(lista))