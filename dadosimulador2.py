import random

print("This is a random dice simulator\nHave fun!")

x = "y"
d1 = " _____________ \n|             |\n|             |\n|      O      |\n||\n|_____________|"
d2 = " _____________ \n|             |\n|          O  |\n|             |\n|  O          |\n|_____________|"
d3 = " _____________ \n|             |\n|          O  |\n|      O      |\n|  O          |\n|_____________|"
d4 = " _____________ \n|             |\n|  O       O  |\n|             |\n|  O       O  |\n|_____________|"
d5 = " _____________ \n|             |\n|  O       O  |\n|      O      |\n|  O       O  |\n|_____________|"
d6 = " _____________ \n|             |\n|  O   O   O  |\n|             |\n|  O   O   O  |\n|_____________|"
d = [d1, d2, d3, d4, d5, d6]

while x == "y":
    number = random.randint(0,5)
    no = random.randint(0,5)
    print("\nRolling Dice....")
    print(d[number])
    print(d[no])
    x = input("Do you want to roll again?[y/n]\n")
