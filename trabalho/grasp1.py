import random;
from pessoa import *;
from par import *;
def definirMinimo(listaMasculina,dicionarioM,listaFeminina,dicionarioF):
    n = len(listaMasculina)
    # randon number
    pareslista = []
    for i in range(0,2*n):
        
        if i < n :
            contador = 0
            if not dicionarioM[listaMasculina[i].getId()].getJaEscolido():
                #print("status H:",listaMasculina[i].getId(),listaMasculina[i].getJaEscolido())
                for proximoPar in listaMasculina[i].getPreferenciaLista():
                
                    possivelPar = dicionarioF[proximoPar]
                    

                    if not possivelPar.getJaEscolido():
                        if contador == 8:
                            inserirListaDeparesOrdenado(pareslista, pares(listaMasculina[i],possivelPar) ) 
                            break   
                        #print("status M:",possivelPar.getId(),possivelPar.getJaEscolido())
                        #break
                        else:
                            contador = contador + 1
                            inserirListaDeparesOrdenado(pareslista, pares(listaMasculina[i],possivelPar) )
            
        else :
            if not dicionarioF[listaFeminina[i-n].getId()].getJaEscolido():
                #print("status M:",listaFeminina[i-n].getId(),listaFeminina[i-n].getJaEscolido())
                for proximoPar in listaFeminina[i-n].getPreferenciaLista():
                    possivelPar = dicionarioM[proximoPar]
                    if not possivelPar.getJaEscolido():
                        #print("status H:",possivelPar.getId(),possivelPar.getJaEscolido())
                        #break
                        if contador == 8:
                            inserirListaDeparesOrdenado(pareslista, pares(possivelPar,listaFeminina[i-n])) 
                            break    
                        else:
                            contador = contador + 1
                            inserirListaDeparesOrdenado(pareslista, pares(possivelPar,listaFeminina[i-n]))       
            
    return  pareslista

def menorNList(Lista,tamanhoNovaLista):
    n = len(Lista)
    if(tamanhoNovaLista >= n):
        return Lista
    menorLista = []
    for i in range(tamanhoNovaLista) :
        menorLista.append(Lista[i])
    #for p in range(len(Lista)- )

def inserirListaDeparesOrdenado(lista,elemento):
    if len(lista) == 0 :
        lista.append(elemento)
        return
    for i in range(len(lista)):
        if elemento.getPontuacao() <= lista[i].getPontuacao() :
            lista.insert(i,elemento)
            return
    lista.append(elemento)
def escolherElementoInListRPC(listaRPC,numero,dicionarioM,dicionarioF):
    if len(listaRPC) < numero:
        numero = len(listaRPC)
    valorAleatoro=random.randrange(0, numero, 1)
    dicionarioM[listaRPC[valorAleatoro].getHomen().getId()].setEscolhido(dicionarioF[listaRPC[valorAleatoro].getMulher().getId()])

    dicionarioF[listaRPC[valorAleatoro].getMulher().getId()].setEscolhido(dicionarioM[listaRPC[valorAleatoro].getHomen().getId()])
    return listaRPC[valorAleatoro]

