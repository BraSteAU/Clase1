#Escribir un programa que:
#Solicite al usuario ingresar 10 numeros
#Almacene solo los numeros pares en un arreglo
#y luego muestre los numeros pares almacenados en el arreglo

numeros=[]
for i in range(10):
    num=int(input(f"Ingrese el numero {i+1} "))
    if num%2==0:
        numeros.append(num)
print("Numeros pares: ",numeros)