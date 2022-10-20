

materias=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas=[]


for materia in materias:
    nota=input("Digite la nota de "+materia+": ")
    notas.append(nota)

for i in range(len(materias)):
    print("En "+materias[i]+" sacaste"+notas[i])