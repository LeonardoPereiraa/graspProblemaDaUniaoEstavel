from pessoa import *;
import random;
def getToFile(arquivoName,dicionario):
    f = open(arquivoName, "r")
    numero = ""
    lista = []
    listaPessoa=[]
    contador = 0

    for linha in f:
        for letra in linha:
            if letra == "," :
                lista.append(int(numero))
                numero = ""
            elif letra != "\n":
                numero = numero + letra
        #print(lista)
        lista.append(int(numero))
        numero = ""
        novaPessoa =pessoa(contador,lista)
        listaPessoa.append(novaPessoa)
        dicionario[contador]= novaPessoa
        contador=contador+1
        lista = []   
    #print(listaPessoa)
    f.close()
    return listaPessoa
def entradasAleatoria(N):
    lista = []
    for i in range(N):
        lista.append(i)
    print(lista)
    numeroDeFaltantes = N
     
    saida=""
    for p in range(N):
        saida=""
        lista1 = []
        for i in range(N):
            aleatorio = random.randrange(0, numeroDeFaltantes, 1)
            numeroDeFaltantes = numeroDeFaltantes -1
            saida = saida + str(lista[aleatorio])
            lista1.append(lista[aleatorio])
            lista.remove(lista[aleatorio])

            if i < N-1 :
                saida = saida + ","
        print(saida)
        numeroDeFaltantes = N
        lista = lista1


#entradasAleatoria(50)
#a = dict()
#getToFile("arqM.txt",a)