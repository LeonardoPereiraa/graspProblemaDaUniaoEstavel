import random;
from pessoa import *;
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

