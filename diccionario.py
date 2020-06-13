import json
from difflib import get_close_matches

data = json.load(open("data.json")) # Abrir archivo json

def translate(word): # Funcion que traduce la palabra
    word = word.lower() # Palabra a minusculas
    if word in data: # Si la palabra esta en el json lo muestra
        return data[word]
    elif word.title() in data: # Si es un titulo lo muestra
        return data[word.title()]
    elif word.upper() in data: # Si la palabra esta en mayus
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 : # Ciclo que usa la funcion get_close_matches para predecir una palabra
        print("did you mean %s instead? " %get_close_matches(word, data.keys())[0]) # Muestra la palabra predecida
        decide = input("press y for yes or n for no: ")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]] # Muestra el resultado del diccionario de la palabra
        elif decide == "n":
            return("You have enter wrong word, please check it again")
        else:
            return("You have entered wrong input please enter just y or n: ")
    else:
        print("You have enter wrong word, please check it again")

word = input("Enter the word you want to watch: ")
output = translate(word)

if type(output) == list: # ciclo para ordenar significados diferentes de una palabra
    for item in output:
        print(item)
else:
    print(output)
