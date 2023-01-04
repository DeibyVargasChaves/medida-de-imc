

peso = float(input("ingresa su peso en kg:"))
estatura = float(input("ingrese su estatura en metros:"))
imc = peso / estatura**2
print(f"Tu indice de masa corporal es {round(imc, 2)}")