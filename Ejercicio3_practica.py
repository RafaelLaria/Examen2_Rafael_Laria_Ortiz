def busqueda_secuencia(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return lista[i]
        else:
            return '-1'

lista1 = [0,120,240,3406,405620,3503,4601,2502,45072404,60]
print(busqueda_secuencia(lista1, 3503))