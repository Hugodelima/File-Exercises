
def buble_sort(lista):
    for i in range(0, len(lista)):
        for j in range(0, i):
            if lista[i].lower() < lista[j].lower():
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
            
arquivo = open('disciplina.txt', 'r')
arquivo2 = open("ordem2.txt", 'w')



frase = arquivo.read().split("\n")

buble_sort(frase)

print(frase)
for i in frase:
    arquivo2.write(str(i) + '\n')



arquivo.close()
arquivo2.close()