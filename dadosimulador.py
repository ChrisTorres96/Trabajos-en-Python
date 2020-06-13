import random

x = "y" # Variable usada como bandera para seguir o no lanzando los dados
print("---Welcome to Dice Simulator---\n\n")
while(x == "y"): # Ciclo que se ejecutara siempre que el usuario desee lanzar los dados
    number = random.randint(1,6) # Generacion de numeros aleatorios entre 1 y 6
    if (number == 1): # Si el numero es 1 imprime lo siguiente
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")

    if (number == 2): # Si el numero es 2 imprime lo siguiente
        print("---------")
        print("|       |")
        print("|  0 0  |")
        print("|       |")
        print("---------")

    if (number == 3): # Si el numero es 3 imprime lo siguiente
        print("---------")
        print("|       |")
        print("| 0 0 0 |")
        print("|       |")
        print("---------")

    if (number == 4): # Si el numero es 4 imprime lo siguiente
        print("---------")
        print("|0     0|")
        print("|       |")
        print("|0     0|")
        print("---------")

    if (number == 5): # Si el numero es 5 imprime lo siguiente
        print("---------")
        print("|0     0|")
        print("|   0   |")
        print("|0     0|")
        print("---------")

    if (number == 6): # Si el numero es 6 imprime lo siguiente
        print("---------")
        print("|0     0|")
        print("|0     0|")
        print("|0     0|")
        print("---------")

    x = input("\nPress y to roll again: ") # Se pregunta al usuario si desea lanzar los dados de nuevo

print("Thank you for playing :)")
