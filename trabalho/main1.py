import random;
from pessoa import *;
from par import *;
from grasp1 import *;
from doisopt import *;
from tool import *;

from file import *;


#m0 = pessoa(0,[0,1,2,3,5,4])
#m1 = pessoa(1,[1,2,0,5,3,4])
#m2 = pessoa(2,[5,0,1,3,4,2])
#m3 = pessoa(3,[0,4,2,1,3,5])
#m4 = pessoa(4,[1,2,0,5,4,3])
#m5 = pessoa(5,[2,3,1,0,5,4])
#f0 = pessoa(0,[1,0,5,2,3,4])
#f1 = pessoa(1,[1,3,4,0,2,5])
#f2 = pessoa(2,[2,0,1,5,4,3])
#f3 = pessoa(3,[1,0,3,2,5,4])
#f4 = pessoa(4,[1,2,0,4,3,5])
#f5 = pessoa(5,[2,3,1,5,4,0])
dicionarioM = dict() 
dicionarioF = dict()
#dicionarioM={0:m0,1:m1,2:m2,3:m3,4:m4,5:m5}
#listaM = [m0,m1,m2,m3,m4,m5]
listaM = getToFile("arqM.txt",dicionarioM)
listaF=getToFile("arqF.txt",dicionarioF)
#dicionarioF ={0:f0,1:f1,2:f2,3:f3,4:f4,5:f5}
#listaF=[f0,f1,f2,f3,f4,f5]

listaGrasp= []
melhorSolucao = []
for i in range( len(listaM)) :
    listaRPC= definirMinimo(listaM,dicionarioM,listaF,dicionarioF)
    listaGrasp.append(escolherElementoInListRPC(listaRPC, 25,dicionarioM,dicionarioF))


#print("estabilidade: ",calculeteTotalEstabilidade(listaGrasp,dicionarioF,dicionarioM))
#print("pontuacao Total:",calculeteTotalPontuetion(listaGrasp))
#printLista(listaGrasp,0)

doisOpt1(listaGrasp,dicionarioF,dicionarioM)

#printLista(listaGrasp,1)

melhorSolucao =  listaGrasp
melhorPontuacao = calculeteTotalPontuetion(melhorSolucao)
melhorEstabilidade = calculeteTotalEstabilidade(melhorSolucao,dicionarioF,dicionarioM)



listaGrasp = []
tempo = 0
resetJaEscolido(listaM)
resetJaEscolido(listaF)
while tempo < 150:
    for i in range( len(listaM)) :
        listaRPC = definirMinimo(listaM,dicionarioM,listaF,dicionarioF)
        listaGrasp.append(escolherElementoInListRPC(listaRPC, 25,dicionarioM,dicionarioF))
    doisOpt1(listaGrasp,dicionarioF,dicionarioM)

    novaPontuacao = calculeteTotalPontuetion(listaGrasp)
    novaEstabilidade = calculeteTotalEstabilidade(listaGrasp,dicionarioF,dicionarioM)
    if novaEstabilidade > melhorEstabilidade :
        melhorSolucao = listaGrasp
        melhorPontuacao = novaPontuacao
        melhorEstabilidade = novaEstabilidade
        
    
    elif novaEstabilidade == melhorEstabilidade and melhorPontuacao > novaPontuacao :
        melhorSolucao = listaGrasp
        melhorPontuacao = novaPontuacao
        melhorEstabilidade = novaEstabilidade
        
        
    listaGrasp = []
    tempo = tempo + 1
    resetJaEscolido(listaM)
    resetJaEscolido(listaF)
print("-------------------------------------------------")
print("melhorEstabilidade: ",melhorEstabilidade)

print("pontuacao Total:",calculeteTotalPontuetion(melhorSolucao))
#printLista(melhorSolucao,0)
