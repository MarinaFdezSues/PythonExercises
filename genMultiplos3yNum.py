def multiplo(v,n):
	return (v%n==0)

def genMnul3():
	n=1
	while(True):
		yield n*3
		n+=1

def genMnum(num):
	mult3=genMnul3()
	while(True):
		n=next(mult3)
		if(multiplo(n,num)==True):
			yield n

num=7
mult3yNum = genMnum(num)
print(next(mult3yNum))
print(next(mult3yNum))
print(next(mult3yNum))
print(next(mult3yNum))