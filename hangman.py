import random

def hangman(): # Funcion del hangman

    word = random.choice(["pugger", "littlepugger", "tiger", "spiderman", "chris", "pokemon"]) # lista de palabras
    validletters = "abcdefghijklmnñopqrstuvwxyz"
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main += letter
            else:
                main = main + "_" + ""
        if main == word:
            print(main)
            print("Felicidades, ganaste! ")
            break
        print("Adivina la palabra: ", main)
        guess = input()

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Ingresa un caracter valido ")
            guess = input()

        if guess not in word:
            turns -= 1
            if turns == 9:
                print("9 turnos restantes")
                print("------------------")
            if turns == 8:
                print("8 turnos restantes")
                print("------------------")
                print("       O          ")
            if turns == 7:
                print("7 turnos restantes")
                print("------------------")
                print("       O          ")
                print("       |          ")
            if turns == 6:
                print("6 turnos restantes")
                print("------------------")
                print("       O          ")
                print("       |          ")
                print("      /           ")
            if turns == 5:
                print("5 turnos restantes")
                print("------------------")
                print("       O          ")
                print("       |          ")
                print("      / \         ")
            if turns == 4:
                print("4 turnos restantes")
                print("------------------")
                print("     \ O          ")
                print("       |          ")
                print("      / \         ")
            if turns == 3:
                print("3 turnos restantes")
                print("------------------")
                print("     \ O /        ")
                print("       |          ")
                print("      / \         ")
            if turns == 2:
                print("2 turnos restantes")
                print("------------------")
                print("     \ O /|        ")
                print("       |          ")
                print("      / \         ")
            if turns == 1:
                print("1 turnos restantes")
                print("Ultimo intento, cuidado!")
                print("------------------")
                print("     \ O_|/       ")
                print("       |          ")
                print("      / \         ")
            if turns == 0:
                print("Perdiste ",name, "!")
                print("Dejaste que el hombre muriera")
                print("------------------")
                print("       O_/       ")
                print("      /|\          ")
                print("      / \         ")
                print(" La palabra era: ", word)
                break

name = input("Ingresa tu nombre: ") # Nombre del usuario

print("Bienvenido ", name)
print("------------------")
print("Intenta adivinar la palabra en menos de 10 intentos ")
hangman()
print()
