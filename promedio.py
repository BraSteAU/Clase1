#Programa que calcule el promedio de calificacion de un grupo de estudiantes
# y determine cuantos aprobaron, teneido en cuenta que la calificacion minima es 6

calificaciones=[]
#pedir calificaciones

n=int(input("Cuantos estudiantes hay? "))
for i in range(n):
    nota=float(input(f"Ingrese la calificacion del estudiante {i+1}"))
    calificaciones.append(nota)

#Calculamos el promedio:
promedio=sum(calificaciones)/len(calificaciones)
aprobados=len([nota for nota in calificaciones if nota>=6])

print(f"Promedio del grupo: {promedio:.2f}")
print(f"Estudiantes aprobados: {aprobados}")