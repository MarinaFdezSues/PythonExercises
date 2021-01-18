def barajaFrancesa():
	bFrC=("as ♥", "1 ♥", "2 ♥","3 ♥","4 ♥", "5 ♥", "6 ♥","7 ♥", "8 ♥","9 ♥","10 ♥", "J ♥", "Q ♥","K ♥")
	bFrR=("as ♦", "1 ♦", "2 ♦","3 ♦","4 ♦", "5 ♦", "6 ♦","7 ♦", "8 ♦","9 ♦","10 ♦", "J ♦", "Q ♦","K ♦")
	bFrT=("as ♣", "1 ♣", "2 ♣","3 ♣","4 ♣", "5 ♣", "6 ♣","7 ♣", "8 ♣","9 ♣","10 ♣", "J ♣", "Q ♣","K ♣")
	bFrP=("as ♠", "1 ♠", "2 ♠","3 ♠","4 ♠", "5 ♠", "6 ♠","7 ♠", "8 ♠","9 ♠","10 ♠", "J ♠", "Q ♠","K ♠")
	bFr=bFrC+bFrP+bFrR+bFrT
	return bFr

def mano(baraja):
	import random
	return random.sample(list(baraja), 5)

def pockerBFr(mano):
	#mano=["12♥","3♥","1♦","1♣","1♠"] #mano auxiliar para comprobar si valida el poker
	print("Mano: ",mano[:])
	for y in mano[0:2]:
		num=y[0:1]
		poker=0
		for x in mano:
			if((num in x)):
				poker=poker+1
		if (poker==4):
			print("Poker!!")
			break
	if(poker<4):
		print("No hay poker.")


print("La baraja francesa es: ",barajaFrancesa())
print()
pockerBFr(mano(barajaFrancesa()))

