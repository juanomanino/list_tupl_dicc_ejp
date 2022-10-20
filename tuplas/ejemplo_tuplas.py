

meses=("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")


salir=False

while not salir:
    num=int(input("Digite un número: "))
    if num==0:
        salir=True
    elif num>1 and num<=len(meses):
        print(meses[num-1])
    else:
        print("Inserta un número entre 1 y ", len(meses))






