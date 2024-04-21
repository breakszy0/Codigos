años_nacimiento = input("Ingresa tu año de nacimiento: ")

años_nacimiento = int(años_nacimiento)

cumpleaños_pasado = input("¿Ya ha tenido su cumpleaños este año? (responde 'si' o 'no'): ")

año_actual = 2024 

if cumpleaños_pasado.lower() == 'si':
    edad = año_actual - años_nacimiento
else:
    edad = año_actual - años_nacimiento - 1

print("Tu edad actual es:", edad, "años")