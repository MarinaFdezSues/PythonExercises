def mcd(a,b):
	if(a<b):
		aux=a
		a=b
		b=aux
	if (b==0):
		return a
	elif(a%b==0):
			return b
	else:
		return(mcd(b,a%b))

print(mcd(406,158))