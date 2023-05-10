def buble_sort(lista):
    for i in range(0, len(lista)):
        for j in range(0, i):
            if lista[i].lower() < lista[j].lower():
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
            
arquivo = open('disciplina.txt', 'r', encoding='utf-8')
arquivo2 = open("ordem5.txt", 'w', encoding='utf-8')

frase = arquivo.readlines()


def busca_palavra(palavra,frase):
    cont = 0
    for i in frase:
        cont = cont+1
        if palavra in i:
            print(i, cont)

palavra = input("Informe uma palavra ")
busca_palavra(palavra,frase)






        
        

        






    
arquivo.close()
arquivo2.close()