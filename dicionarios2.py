def diccionarios1(cadena):
    print(cadena)
    #se deja bonito
    cadena=cadena.replace('¡' ,'' ).replace('!' ,'' ).replace('#' ,'' ).replace('@' ,'' ).replace('€','').replace('¿' ,'' ).replace('?' ,'' ).replace(',' ,'' ).replace('.' ,'' )
    #se pasa a minúsculas y se crea una lista de palabras
    lista=cadena.lower().split()
    #se pone cada palabra como clave y su número de apariciones como valor
    dic={l : lista.count(l) for l in lista}
    return dic


#cadena = "Una cadena y una prueba"
#cadena = "#qUITo@ ¡varias@! ¿co€sas? varias."
cadena = "Mi casa, mi coche y mi otro coche"
print(diccionarios1(cadena))
print()