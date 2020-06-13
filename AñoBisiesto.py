year = int(input("Escribe el año para checar si es bisiesto\n"))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} es año bisiesto".format(year))
        else:
            print("{0} NO es año bisiesto".format(year))
    else:
        print("{0} es año bisiesto".format(year))
else:
    print("{0} NO es año bisiesto".format(year))
                
