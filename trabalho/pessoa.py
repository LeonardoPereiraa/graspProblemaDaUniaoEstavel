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
