print ("Dime la temperatura de tu bebida")
temp_bebida = int(input())
if temp_bebida < 50:
  print("Debes esperar a que se caliente la bebida")
elif temp_bebida >=50 and temp_bebida <= 70:
  print("Se puede servir de inmediato")
if temp_bebida > 70:
  print("La bebida está muy caliente, espera a que se enfríe")


print("Dime la hora en un formato de 24 horas")
hora = float(input())
if hora >= 6 and hora <=11:
  print("Las bebidas calientes se sirven más rápido")
else:
  print("Espera el turno")
  

print("¿Que tipo de bebida prefiere? café, té o chocolate")
bebida = str(input())
print("Dime la hora en un formato de 24 horas")
hora = float(input())

if bebida == "café" or bebida == "té" and hora >=7 and hora <=9:
    print("Te recomendamos una bebida caliente")

elif (bebida == "té" or bebida == "chocolate") and hora >=12 and hora <=14:
  print("Te recomendamos una bebida fría")

