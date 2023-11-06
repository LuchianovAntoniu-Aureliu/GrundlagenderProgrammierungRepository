def ex5(lista, expresie):
    lista_noua = []
    for element in lista:
        x = element // 10
        y = element % 10
        if eval(expresie):
            lista_noua.append(element)
    return lista_noua


lista_to_check = [93, 42 ,65 ,10]
expression = "x==y*2"
res = ex5(lista_to_check, expression)
print(res)
