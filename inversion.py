#Programa que solicite una lista de 5 elementos al usuario
#Imprima la lista en orden inverso

arreglo = []
for i in range(5):
    valor=input(f"Ingrese un valor para el areglo en la posicion {i+1}: " )
    arreglo.append(valor)
print(f"El arreglo original es: {arreglo}")
print(f"El arreglo invertio es: {arreglo[::-1]}")  #incio:fin:paso