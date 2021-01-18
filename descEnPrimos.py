#Implementar una función que reciba un numero y devuelva su descomposición en números primos
import math

def descEnPrimos(num):
	divisores=divisoresPrimos(num)
	factores=[]
	for divisor in divisores:
		while(num%divisor==0):
			num/=divisor
			factores.append(divisor)
	return factores

def sigPrimo(n):
	while(True):
		n+=1
		if (primo(n)):
			return n

def primo(n):
	es_primo=True
	i=2
	while (primo and i<=math.sqrt(n)):
		if (n%i==0):
			es_primo=False
		i+=1
	return es_primo

def divisoresPrimos(num):
	divisores=[]
	primo=2
	while(primo<num):
		resto=num%primo
		if (resto==0):
			divisores.append(primo)
		primo=sigPrimo(primo)
	return divisores

numero = 588
print(numero, ' se descompone en:',descEnPrimos(numero))
