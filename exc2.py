
arquivo = open('texto2.txt', 'r')
for i in arquivo:
    frase = i
    for j in frase:
        print(j)
        print(ord(str(j)))


arquivo.close()