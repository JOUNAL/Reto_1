# Reto 1
# Programación Orientada a Objetos - UNAL



## Reto 1.1

Para este caso use un case segun la operacion aritmetica introducida por el usuario, y despues de eso en cada case correspondiente se hacia la accion correspondiente.
```python
num1= int(input("Digite los numeros a operar:"))
num2= int(input())
operacion= str(input("Digite la operacion a realizar:"))
match operacion:
    case "+":
        print("El resultado de la operacion es:" + str(num1 + num2))
    case "-":
        print("El resultado de la operacion es:" + str(num1 - num2))
    case "*":
        print("El resultado de la operacion es:" + str(num1 * num2))
    case "/":
        print("El resultado de la operacion es:" + str(num1 / num2))
```


### Componentes del Ciclo `while`
- Condición de parada: Evalúa si el bloque de instrucciones debe ejecutarse.
- Bloque de instrucciones: Conjunto de instrucciones que se ejecutan mientras la condición sea verdadera.
- Actualización: Modificación de variables para que eventualmente la condición de parada sea falsa y termine el ciclo.

## Reto 1.2

Para el palindromo use una division entera para tener donde esta la mitad, y entera porque si es impar no tomara en cuenta la letra de la mitad, despues tomara esa longitud y la compara con la primera y la ultima, se le suma 1 a la primera y se le resta 1 a la ultima, asi hasta que llegue a la mitad dada por la division entera

```python
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
```

## Reto 1.3

Para este caso considere que introducia una lista de numeros, tendria que tener al final una lista que solo eran primos y para saber si era primo utilice un contador de 2 hasta el numero-1 y si todas las veces que con la operacion modular da diferente de 0, se añade a la lista prima

```python
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
```

## Reto 1.4

La idea era ir sumando numero por numero en la lista, y si la suma era mas grande que la de los anteriores numeros, guardaba esa suma y la posicion de los numeros de esa suma, para despues imprimirlos

```python
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

```
## Reto 1.5

La idea era que por cada palabra hiciera una lista de las letras sin que se repitiera, despues esa lista de esa palabra se compararia con cada palabra, y si se verificaba que la cantidad de letras de la palabra a escanear era igual a su longitud comparada con la lista de letras, entonces esa palabra tenia las mismas letras y su posicion se añadia a una lista, y si esa palabra se repetia mas de una vez en la lista, se imprimia

```python
lista_palabras=[]
palabras_bien=[]
palabra_base: str
palabra_ahora: str
letra: str
i=0
g=0
d=0
no_vacio=True
while no_vacio==True:
    palabra= str(input("Digite las palabras que quiera evaluar que tengan los mismos caracteres; o deje el cambio vacio para terminar:"))
    if palabra !="":
        lista_palabras.append(palabra)
    else:
        break
    

while i<len(lista_palabras):
    palabra_base=lista_palabras[i]
    j=0
    palabra_letras=[]
    c=0
    while c<len(palabra_base):
        palabra_letras.append(palabra_base[c])
        c +=1
    c=0
    while c<len(palabra_letras):
        d=0
        h=0
        while h<len(palabra_letras):
            a=palabra_letras[h]
            b=palabra_letras[c]
            if palabra_letras[h]==palabra_letras[c]:
                
                d +=1
            if d>1:
                palabra_letras.pop(h)
                h -=1
                d -=1
            h +=1
        c +=1
    
    while j<len(lista_palabras):
        palabra_ahora=lista_palabras[j]
        k=0

        t=0
        while k<len(palabra_letras):
            w=0
            
            while w<len(palabra_ahora):
                if (palabra_letras[k]==palabra_ahora[w])==True:
                    t +=1
            
                w +=1
            k +=1
        if t==len(palabra_ahora):
            palabras_bien.append(j)
        j +=1
    i +=1


c=0

i=len(palabras_bien)
while c<i:
    h=0
    d=0
    while h<i:
        a=palabras_bien[h]
        b=palabras_bien[c]
        if palabras_bien[h]==palabras_bien[c]:
            d+=1
        h +=1
    if d==1:
        palabras_bien.pop(c)
        i=len(palabras_bien)
        c -=1
    c+=1 

c=0
i=len(palabras_bien)
while c<i:
    h=0
    d=0
    while h<i:
        a=palabras_bien[h]
        b=palabras_bien[c]
        if palabras_bien[h]==palabras_bien[c]:
            d+=1
        h +=1
    if d>1:
        palabras_bien.pop(c)
        i=len(palabras_bien)
        c -=1
    c+=1 

c=0
i=len(palabras_bien)
while c<i:
    print(lista_palabras[palabras_bien[c]])
    c+=1
```
