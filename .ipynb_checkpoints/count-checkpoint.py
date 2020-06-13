def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

if __name__ == '__main__':     # Se agrega esto para correr el programa como script y asi testee el codigo
    print (linecount('count.py'))
