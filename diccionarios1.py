def diccionarios1(lista):
    print(lista)
    dic={l[0] : l[1:] for l in lista}
    return dic

def diccionarios1extra(l):
    dic={}
    print(l)
    for x in l:
    	key=x[0]
    	values=list(x[1:])
    	dic[key]=values
    return dic

def extraDicc1(l):
	dic={}
	k=l[0]
	v=l[1]
	for x in range(0,len(k)):
		try:
			dic[k[x]]=v[x]
		except Exception as e:
			dic[k[x]]=""
	print(dic)

def extraDicc2(l):
    keys=l[0]
    values=l[1]
    dic= dict(zip(keys,values))
    return dic
	
#lista = [("a","b","c","d"),("A","B","C","D")]
#lista = [(1,2),(3,4)]
lista = [(1,2,3), ("A","B","C",4)]
print(diccionarios1(lista))
print()