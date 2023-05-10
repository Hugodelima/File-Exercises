



arquivo = open('texto3.txt', 'w')
arquivo2 = open('texto2.txt', 'r')

inverso = arquivo2.read()
inverso = inverso[::-1]
arquivo.write(inverso)


arquivo.close()
arquivo2.close()