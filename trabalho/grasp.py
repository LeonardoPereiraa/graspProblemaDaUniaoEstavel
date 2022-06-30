import random;
class pessoa:
    def __init__(self, id,preferenciaLista):
        self._id = id
        self._preferenciaLista = preferenciaLista
        self._par = None
        self.escolidoo = False
    def getId(self):
        return self._id  
    def getPreferenciaLista(self):
        return self._preferenciaLista
    def getPar(self):
        return self._par
    def setPar(self, novoPar):
        self._par=novoPar
    def getElemetoPreferenciaLista(self, posissao):
        return self._preferenciaLista[posissao]
    def getPosissaoInPreferenciaLista(self,elementId):
        for i in range(0,len(self._preferenciaLista)):
            if elementId == self._preferenciaLista[i] :
                return i
        return None
    def getJaEscolido(self):
        return self.escolidoo
    def setNaoEscolhido(self):
        self.escolidoo = False
    def setEscolhido(self,par):
        self.escolidoo = True
        self.setPar(par)
class pares:
    def __init__(self, homen,mulher):
        self._homen = homen
        #homen.setPar(mulher) 
        self._mulher = mulher
        #mulher.setPar(homen)
        self.redifinePontuacao()
        #self._pontuacao = homen.getPosissaoInPreferenciaLista(mulher.getId()) + mulher.getPosissaoInPreferenciaLista(homen.getId())
    def getHomen(self):
        return self._homen
    def getMulher(self):
        return self._mulher
    def setHomen(self,novoHomem):
        self._homen = novoHomem
        self.redifinePontuacao()
    def setMulher(self, novaMulher):
        self._mulher = novaMulher
        self.redifinePontuacao()
    def getPontuacao(self):
        return self._pontuacao
    def redifinePontuacao(self):
        self._pontuacao = self._homen.getPosissaoInPreferenciaLista(self._mulher.getId()) + self._mulher.getPosissaoInPreferenciaLista(self._homen.getId())

def definirMinimo(listaMasculina,dicionarioM,listaFeminina,dicionarioF):
    n = len(listaMasculina)
    # randon number
    pareslista = []
    for i in range(0,2*n):
        
        if i < n :
            if not dicionarioM[listaMasculina[i].getId()].getJaEscolido():
                #print("status H:",listaMasculina[i].getId(),listaMasculina[i].getJaEscolido())
                for proximoPar in listaMasculina[i].getPreferenciaLista():
                
                    possivelPar = dicionarioF[proximoPar]
                    if not possivelPar.getJaEscolido():
                        #print("status M:",possivelPar.getId(),possivelPar.getJaEscolido())
                        #break
                        inserirListaDeparesOrdenado(pareslista, pares(listaMasculina[i],possivelPar) )
            
        else :
            if not dicionarioF[listaFeminina[i-n].getId()].getJaEscolido():
                #print("status M:",listaFeminina[i-n].getId(),listaFeminina[i-n].getJaEscolido())
                for proximoPar in listaFeminina[i-n].getPreferenciaLista():
                    possivelPar = dicionarioM[proximoPar]
                    if not possivelPar.getJaEscolido():
                        #print("status H:",possivelPar.getId(),possivelPar.getJaEscolido())
                        #break
                    
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
    while contador < 50 :
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


m0 = pessoa(0,[0,1,2,3,5,4])
m1 = pessoa(1,[1,2,0,5,3,4])
m2 = pessoa(2,[5,0,1,3,4,2])
m3 = pessoa(3,[0,4,2,1,3,5])
m4 = pessoa(4,[1,2,0,5,4,3])
m5 = pessoa(5,[2,3,1,0,5,4])
f0 = pessoa(0,[1,0,5,2,3,4])
f1 = pessoa(1,[1,3,4,0,2,5])
f2 = pessoa(2,[2,0,1,5,4,3])
f3 = pessoa(3,[1,0,3,2,5,4])
f4 = pessoa(4,[1,2,0,4,3,5])
f5 = pessoa(5,[2,3,1,5,4,0])
dicionarioM = dict() 
dicionarioF = dict()
dicionarioM={0:m0,1:m1,2:m2,3:m3,4:m4,5:m5}
listaM = [m0,m1,m2,m3,m4,m5]
dicionarioF ={0:f0,1:f1,2:f2,3:f3,4:f4,5:f5}
listaF=[f0,f1,f2,f3,f4,f5]

listaGrasp= []
melhorSolucao = []
for i in range( len(listaM)) :
    listaRPC= definirMinimo(listaM,dicionarioM,listaF,dicionarioF)
    listaGrasp.append(escolherElementoInListRPC(listaRPC, 15,dicionarioM,dicionarioF))


#print("estabilidade: ",calculeteTotalEstabilidade(listaGrasp,dicionarioF,dicionarioM))
#print("pontuacao Total:",calculeteTotalPontuetion(listaGrasp))
#printLista(listaGrasp,0)

doisOpt(listaGrasp,dicionarioF,dicionarioM)

#printLista(listaGrasp,1)

melhorSolucao =  listaGrasp
melhorPontuacao = calculeteTotalPontuetion(melhorSolucao)
melhorEstabilidade = calculeteTotalEstabilidade(melhorSolucao,dicionarioF,dicionarioM)



listaGrasp = []
tempo = 0
resetJaEscolido(listaM)
resetJaEscolido(listaF)
while tempo < 100:
    for i in range( len(listaM)) :
        listaRPC = definirMinimo(listaM,dicionarioM,listaF,dicionarioF)
        listaGrasp.append(escolherElementoInListRPC(listaRPC, 15,dicionarioM,dicionarioF))
    doisOpt(listaGrasp,dicionarioF,dicionarioM)

    novaPontuacao = calculeteTotalPontuetion(listaGrasp)
    novaEstabilidade = calculeteTotalEstabilidade(listaGrasp,dicionarioF,dicionarioM)
    if novaEstabilidade > melhorEstabilidade :
        melhorSolucao = listaGrasp
        melhorPontuacao = novaPontuacao
        melhorEstabilidade = novaEstabilidade
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("melhorEstabilidade: ",melhorEstabilidade)
        print("melhorPontuacao: ",melhorPontuacao)
        print("estabilidade: ",calculeteTotalEstabilidade(melhorSolucao,dicionarioF,dicionarioM))
        print("pontuacao Total:",calculeteTotalPontuetion(melhorSolucao))
        printLista(melhorSolucao,0)
    
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
#print("melhorPontuacao: ",melhorPontuacao)
print("pontuacao Total:",calculeteTotalPontuetion(melhorSolucao))
printLista(melhorSolucao,0)
    #print("homen:",listaGrasp[i].getHomen().getId(),"Mulher:",listaGrasp[i].getMulher().getId(),"pontuacao:",listaGrasp[i].getPontuacao())
#definirMinimo(listaM,listaF)
#for p in range(len(listaGrasp)):
    
#    print("homen:",listaGrasp[p].getHomen().getId(),"Mulher:",listaGrasp[p].getMulher().getId(),"pontuacao:",listaGrasp[p].getPontuacao())
#    print("par Estavel: ",verificarEstabilidadeDedoisNó(listaGrasp[p],dicionarioF,dicionarioM) )

