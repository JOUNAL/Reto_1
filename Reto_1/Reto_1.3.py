lista_total=[]
lista_prima=[]
i: int=0
valor=0
numero=True
while numero==True:
    nuevo_numero= input("Digite numeros para verificar si son primos, o una letra para parar:")
    if nuevo_numero.isnumeric()==True:
        lista_total.append(nuevo_numero)
    else:
        break
while i<len(lista_total):
    j: int=2
    while j < int(lista_total[i]):
        if int(lista_total[i]) % j != 0:
            j +=1
            if j==int(lista_total[i]):
                lista_prima.append(lista_total[i])
        else:
            break
    i +=1
i=0
while i<len(lista_prima):
    print(lista_prima[i])
    i +=1