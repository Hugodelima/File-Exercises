arquivo = open('texto.txt', 'r')

frase = arquivo.read().split()

for i in frase:
    contador = 0
    if len(i) > 1:
        for j in frase:
            if i == j:
                contador+=1
        print('palavra:', i, 'encontrada: ', contador, 'vezes.')       
    else:
        print('não é palavra')

arquivo.close()