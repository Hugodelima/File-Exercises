def buble_sort(lista):
    for i in range(0, len(lista)):
        for j in range(0, i):
            if lista[i].lower() < lista[j].lower():
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
            
arquivo = open('disciplina.txt', 'r', encoding='utf-8')
arquivo2 = open("ordem3.txt", 'w', encoding='utf-8')

frase = arquivo.readlines()

qtd = len(frase[0])
p = frase[0]
for i in frase:
    if len(i) > qtd:
        qtd = len(i)
        p = i

print(p,qtd)


        
        

        






    
arquivo.close()
arquivo2.close()