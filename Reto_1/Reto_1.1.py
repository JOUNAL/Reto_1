num1= int(input("Digite los numeros a operar:"))
num2= int(input())
operacion= str(input("Digite la operacion a realizar:"))
def Operaciones(numero1,numero2,opera):
    match opera:
        case "+":
            return (numero1 + numero2)
        case "-":
            return(numero1 - numero2)
        case "*":
            return(numero1 * numero2)
        case "/":
            return (numero1 / numero2)
print("El resultado de la operacion es:" + str(Operaciones(num1,num2,operacion)))
