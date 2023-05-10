arquivo = open('texto.txt', 'r')




count = 0
caracteres = 0
for i in arquivo:
    frase = i
    for j in frase:
        if j == 'a':
            count = count+1
        elif j == 'e':
            count = count+1
        elif j == 'i':
            count = count+1
        elif j == 'o':
            count = count+1
        elif j == 'u':
            count = count+1
        elif j == '':
            continue
        else:
            caracteres = caracteres + 1
print('quantidade de vogas são', count)
print('quantidade de caracters são', count + caracteres)
    
    

arquivo.close()