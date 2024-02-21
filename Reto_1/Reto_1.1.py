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