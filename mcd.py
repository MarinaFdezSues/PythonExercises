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

a = int(input())
b = int(input())
print(mcd(a,b))