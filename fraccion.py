class Fraccion ():

	def __init__(self, dd, ds):
		self.dividendo = dd
		self.divisor = ds

	def getDividendo(self): return self.dividendo

	def getDivisor(self): return self.divisor

	def __str__(self): 
		if (self.getDivisor()==1): return f'{self.getDividendo()}'
		else: return f'{self.getDividendo()}/{self.getDivisor()}'

	def sumar(self, f2):
		return Fraccion(self.getDividendo()+f2.getDividendo(), self.getDivisor()+f2.getDivisor())

	def multiplicar(self, f2):
		return Fraccion(self.getDividendo()*f2.getDividendo(), self.getDivisor()*f2.getDivisor())

	def simplicar(self):
		f = self
		m = f.fracMcd()
		f = Fraccion(int(f.getDividendo() / m), int(f.getDivisor() / m))
		return f

	def fracMcd(self):
		dd = self.getDividendo()
		ds = self.getDivisor()
		if(dd<ds):
			aux=dd
			dd=ds
			ds=aux
		if (ds==0):
			return dd
		elif(dd%ds==0):
				return ds
		else:
			return(Fraccion(ds,dd%ds).fracMcd())

def prueba():
	f1 = Fraccion(10,2)
	f2 = Fraccion(8,5)
	print(f'{f1} + {f2} = {f1.sumar(f2)}')
	f3 = f1.multiplicar(f2)
	print(f'{f1} * {f2} = {f3}')
	print(f'{f3} = {f3.simplicar()}' )

prueba()