lista_numeros=[]
i: int=0
valor=0
valor_m=0
posicion=0
numero=True
while numero==True:
    nuevo_numero= input("Digite la lista de numeros; o una letra para parar:")
    if nuevo_numero.isnumeric()==True:
        lista_numeros.append(nuevo_numero)
    else:
        break

while i<len(lista_numeros)-1:
    valor=int(lista_numeros[i])+int(lista_numeros[i+1])
    if valor>valor_m:
        valor_m=valor
        posicion=i
    i +=1

print("Los numeros que dan la suma de mayor valor son " + str(lista_numeros[posicion]) + " y " + str(lista_numeros[posicion+1]) + " y el valor es:" + str(valor_m))
