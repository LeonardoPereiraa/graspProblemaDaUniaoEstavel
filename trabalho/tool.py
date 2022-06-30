import random;
from pessoa import *;
from par import *;
from grasp1 import *;
from doisopt import *;




def calculeteTotalEstabilidade(listaPares,dicionarioF,dicionarioM):
    contador = 0
    for i in range(len(listaPares)):
        if verificarEstabilidadeDedoisNó(listaPares[i], dicionarioF,dicionarioM):
            contador = contador +1
    return contador
def calculeteTotalPontuetion(listaPares):
    total = 0 
    for i in range(len(listaPares)):
        total = total + listaPares[i].getPontuacao() 
    return total

def resetJaEscolido(lista):
    for i in range(len(lista)):
        lista[i].setNaoEscolhido()

def printLista(lista, loop):
    print(loop)
    for i in range(len(lista)):
        print("homen:",lista[i].getHomen().getId(),lista[i].getHomen().getJaEscolido(),"Mulher:",lista[i].getMulher().getId(),lista[i].getMulher().getJaEscolido(),"pontuacao:",lista[i].getPontuacao())

