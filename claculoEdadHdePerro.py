print("CALCULO EDAD HUMANA DE UN PERRO")
print("")


strEdad = 0

while strEdad == 0:
    strEdad = input("Introduce la edad del perro: ")
    if not strEdad.isdigit():
        print("La edad del perro debe ser un número entero")
        strEdad = 0
        
edad = int(strEdad)

edadHumana = edad * 7
        
print("Si la edad del perro es {} años, corresponde a {} años humanos" .format(edad, edadHumana))
   