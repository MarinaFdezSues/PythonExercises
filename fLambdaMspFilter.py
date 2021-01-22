areaTriangulo = lambda base, altura: (base * altura) / 2

print('areaTriangulo: ', areaTriangulo(2,4))

lista = [2, 6, 19, 24]
lista2 = map(lambda n: n * 5, lista)

print('lista de numeros * 5: ', list(lista2))

lista3 = filter(lambda n: n % 3 == 0, lista)

print('lista de numeros filtrados multiplos 3: ', list(lista3))
