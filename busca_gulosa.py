#Pedro Catelan

from vetor_ordenado import VetorOrdenado
from mapa import Mapa

class Busca_gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False
        
    def buscar(self, atual):
        print("\nAtual: {}" .format(atual.nome))
        atual.visitado = True
        
        if atual == self.objetivo:
            self.achou = True
        else: 
            self.fronteira = VetorOrdenado(len(atual.adjacentes))
            for i in atual.adjacentes:
                if i.cidade.visitado == False:
                    i.cidade.visitado = True
                    self.fronteira.inserir(i.cidade)
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                Busca_gulosa.buscar(self, self.fronteira.getPrimeiro())


mapa = Mapa()
gulosa = Busca_gulosa(mapa.Bucharest)
gulosa.buscar(mapa.Arad)