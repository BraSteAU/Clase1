#Estructuras de datos...

#El tipo comun y fundamental es el arreglo, este se usa para
#manejar colecciones de elementos

#Definicion:
#   Un arrego es una estructura que almacena elementos del mismo tipo
#   los organiza en posiciones de memoria que son contiguas, permite acceder a los items por medio de un indice.


#1) Acceso rapido en la info por medio de un indice.
#Cualquier elemento puede ser accedido directamente con el indice, lo que toma un tiempo de magnitud constante

arreglo=[10,20,30,40,50]
print("El elemento en el indice 2 es:",arreglo[-1])


#Homogeneidad:

#En lenguajes como c, todos los elementos deben ser del mismo tipo...
#pero python permite mezclar tipos, pero si hay un proposito estricto, es mejor
#usar elementos homogeneos

array=[1,2,3]
print(array)
array.append(4)
print(array)
array.pop(2)
print(array)
print(len(array))

#Operaciones fundamentales de los arreglos

#1)Crear y llenar arregos

arr=[]
#Llenar con 5 valores un arreglo, estos valores los debe ingresar el usuario

for i in range(5):
    valor=int(input(f"Ingrese un numero para la posicion {i}: "))
    arr.append(valor)
print(f"El arreglo finalmente queda: {arr}")


#Recorrer el arreglo
#los arreglos se recorren o iteran con los ciclos for o while, lo mas comun es hacerlo con el ciclo for

print("Elementos del arreglo")
for i in range(len(arreglo)):
    print(f"indice {i},: {arreglo[i]}")


#Modificar elementos internos de los arreglos

layout=[1,2,3,4,5]
print("Elementos del arreglo antes de la modificacion: ",layout)
layout[2]=3.1416
print("Elementos del arreglo despues de la modificacion: ",layout)


#eliminacion
#Se puede hacer de dos maneras dependiendo del parametro que quiera usar para eliminar
#podemos eliminar por indice o eliminar por elemento

#eliminar por indice(pop) elimina el ultimo elemento o elimina el lemnto en la posicion indicada
layout.pop(1)
print("Elementos del arreglo despues de la eliminacion por indice: ",layout)

#eliminar por elemento(remove) elimina el primer elemento que encuentre que coincida con el valor que se le indique
layout.remove(4)
print("Elementos del arreglo antes de la eliminacion por eleme  nto: ",layout)


#aritmetica con arreglos:

pepito=[5,10,15,20,25]
suma=sum(pepito)
promedio=suma/len(pepito)
maximo=max(pepito)
minimo=min(pepito)

print(f"suma: {suma}, promedio: {promedio}, maximo: {maximo}, minimo: {minimo}")









