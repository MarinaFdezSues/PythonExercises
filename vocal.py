def  vocal(letra):
    if (letra in ("a", "e","i","o","u")): 
    	resultado = "\"" + letra + "\"" + " es una vocal"
    else :
    	resultado = " NO es una vocal"
    return resultado

print(vocal("a"))

print(vocal(0))

print(vocal("o"))

print(vocal("c"))
