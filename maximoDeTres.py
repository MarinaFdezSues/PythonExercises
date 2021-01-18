def mayor (n1, n2, n3):
#	print(n1+n2)
	if (n1>n2):
		if (n1>n3):
			return(n1)
		else:
			return(n3)
	elif(n2>n3):
		return(n2)
	else:
		return(n3)
def mayor2 (n1,n2,n3):
	if (n1>n2 and n1>n3):
		return(n1)
	elif(n2>n3):
		return(n2)
	else:
		return(n3)

print("El mayor es: ", mayor2(1,2,3))

print("El mayor es: ", mayor2(5,7,6))

print("El mayor es: ", mayor2(16,11,32))

print("El mayor es: ", mayor2(21,43,10))