import random;
from pessoa import *;
from par import *;
from grasp1 import *;
def verificarEstabilidadeDedoisNó(ParDeNos, dicionarioF,dicionarioM):
    homen = ParDeNos.getHomen()
    mulher = ParDeNos.getMulher()
    posissaoMulher = mulher.getPosissaoInPreferenciaLista(homen.getId())
    posissaoHomen = homen.getPosissaoInPreferenciaLista(mulher.getId())
    for i in range(posissaoHomen):
        desafiante = dicionarioF[i].getPar()
        if dicionarioF[i].getPosissaoInPreferenciaLista(homen.getId()) <  dicionarioF[i].getPosissaoInPreferenciaLista(desafiante.getId()):
            #print(dicionarioF[i].getPosissaoInPreferenciaLista(homen.getId()),"<",dicionarioF[i].getPosissaoInPreferenciaLista(desafiante.getId()))
            #print(dicionarioF[i].getId(),"mulher  ", homen.getId() ,"<",desafiante.getId())
            return False
    for i in range(posissaoMulher):
        desafiante = dicionarioM[i].getPar()
        if dicionarioM[i].getPosissaoInPreferenciaLista(mulher.getId()) <  dicionarioM[i].getPosissaoInPreferenciaLista(desafiante.getId()):
            #print(dicionarioM[i].getPosissaoInPreferenciaLista(mulher.getId()),"<", dicionarioM[i].getPosissaoInPreferenciaLista(desafiante.getId()))
            #print(dicionarioM[i].getId(),"Homen  ", mulher.getId(),"<",desafiante.getId())
            return False
    return True 

def comutarPar(par1,par2):
    mulher1 = par1.getMulher()
    mulher2 = par2.getMulher()
    homen1 = par1.getHomen()
    homen2 = par2.getHomen()
    par1.setMulher(mulher2)
    par2.setMulher(mulher1)
    mulher1.setPar(homen2)
    homen1.setPar(mulher2)
    mulher2.setPar(homen1)
    homen2.setPar(mulher1)

def MelhoraDeestabilidadeEntredoisNo(par1,par2,dicionarioF,dicionarioM):
    contador = 0 
    if not verificarEstabilidadeDedoisNó(par1,dicionarioF,dicionarioM) :
        contador = contador +1
    if not verificarEstabilidadeDedoisNó(par2,dicionarioF,dicionarioM) :
        contador = contador +1
    return contador

def pontuacaoParaTroca(par1,par2,dicionarioF,dicionarioM):
    valor = 1000 * MelhoraDeestabilidadeEntredoisNo(par1,par2,dicionarioF,dicionarioM)
    valor = valor + par1.getPontuacao() + par2.getPontuacao()
    return valor
def doisOpt(listaPares,dicionarioF,dicionarioM):
    tamanho = len(listaPares)
    contador = 0 
    melhorPontuacao = 0
    no1 =None 
    no2 = None
    while contador < 200 :
        rand1 = random.randrange(0, tamanho, 1)
        rand2 = random.randrange(0, tamanho, 1)
        if rand1 == rand2 :
            if rand2 > 0 :
                rand2 = rand2 -1
            else:
                rand2 = 1
        pontuacaoAndes = pontuacaoParaTroca(listaPares[rand1],listaPares[rand2],dicionarioF,dicionarioM)
        comutarPar(listaPares[rand1],listaPares[rand2])
        pontuacaoDepois = pontuacaoParaTroca(listaPares[rand1],listaPares[rand2],dicionarioF,dicionarioM)
        
        if melhorPontuacao < pontuacaoAndes - pontuacaoDepois :
            #print("pontos",melhorPontuacao,pontuacaoAndes,"-", pontuacaoDepois ,"= ",pontuacaoAndes- pontuacaoDepois ,"p:", rand1,rand2 )
            melhorPontuacao = pontuacaoAndes - pontuacaoDepois
            no1 = rand1
            no2 = rand2 
            contador = 0            
        else:
            contador = contador +1
        comutarPar(listaPares[rand1],listaPares[rand2])
    if no1 != None :
        #print("mudou",no1,no2)
        comutarPar(listaPares[no1],listaPares[no2])
 






def doisOpt1(listaPares,dicionarioF,dicionarioM):
    tamanho = len(listaPares)
    contador = 0 
    melhorPontuacao = 0
    no1 =None 
    no2 = None
    while contador < 200 :
        rand1 = random.randrange(0, tamanho, 1)
        rand2 = random.randrange(0, tamanho, 1)
        if rand1 == rand2 :
            if rand2 > 0 :
                rand2 = rand2 -1
            else:
                rand2 = 1
        pontuacaoAndes = pontuacaoParaTroca(listaPares[rand1],listaPares[rand2],dicionarioF,dicionarioM)
        comutarPar(listaPares[rand1],listaPares[rand2])
        pontuacaoDepois = pontuacaoParaTroca(listaPares[rand1],listaPares[rand2],dicionarioF,dicionarioM)
        
        if melhorPontuacao < pontuacaoAndes - pontuacaoDepois :
            #print("pontos",melhorPontuacao,pontuacaoAndes,"-", pontuacaoDepois ,"= ",pontuacaoAndes- pontuacaoDepois ,"p:", rand1,rand2 )
            melhorPontuacao = pontuacaoAndes - pontuacaoDepois
            no1 = rand1
            no2 = rand2 
            contador = 0            
        else:
            contador = contador +1
            comutarPar(listaPares[rand1],listaPares[rand2])
    #if no1 != None :
        #print("mudou",no1,no2)
    #    comutarPar(listaPares[no1],listaPares[no2])
 