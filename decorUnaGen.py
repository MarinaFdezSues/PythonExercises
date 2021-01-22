# Implementar un decorador que convierte cualquier función unaria en un generador que recibe un valor inicial.
# Ejercicio pospuesto
def decoradorUnaGEn(funcion):
    def decorar(*args):
        return genpot(funcion(*args))
    return decorar


def genpot(a): yield print(a)

@decoradorUnaGEn
def potencia(b,e): return pow(b,e)

b = int(input('base: '))
e = int(input('exponente: '))#
#print(potencia1(b, e))

print(potencia(b,e))