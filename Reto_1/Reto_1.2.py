def palindromo(var1):
    i:int=0
    j:int=0
    longitud=int(len(palabra))
    j=longitud//2
    while i < j:
        if palabra[i]==palabra[longitud-(1+i)]:
            i+=1
        else:
            return (palabra + " no es un palindromo")
    return (palabra + " es un palindromo")

palabra= str(input("Digite la palabra a validar:"))
print(palindromo(palabra))