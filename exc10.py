def buble_sort(lista):
    for i in range(0, len(lista)):
        for j in range(0, i):
            if lista[i].lower() < lista[j].lower():
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
            
arquivo = open('disciplina.txt', 'r', encoding='utf-8')
arquivo2 = open("ordem10.txt", 'w', encoding='utf-8')




x = arquivo.read().upper()
arquivo2.write(str(x))






        
        

        






    
arquivo.close()
arquivo2.close()