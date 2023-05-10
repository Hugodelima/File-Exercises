
def buble_sort(lista):
    for i in range(0, len(lista)):
        for j in range(0, i):
            if lista[i].lower() < lista[j].lower():
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
            
arquivo = open('texto.txt', 'r')
arquivo2 = open("ordem.txt", 'w')



frase = arquivo.read().split()
buble_sort(frase)

for i in frase:
    arquivo2.write(str(i)+" ")

print(frase)






arquivo.close()
arquivo2.close()