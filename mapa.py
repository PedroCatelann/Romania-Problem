#Pedro Catelan

from cidade import Cidade
from adjacente import Adjacente

class Mapa:
    Arad = Cidade('Arad',366)
    Craiova = Cidade('Craiova',160)
    Dobreta = Cidade('Dobreta',242)
    Eforie = Cidade('Eforie',161)
    Fagaras = Cidade('Fagaras',176)
    Giurgiu = Cidade('Giurgiu',77)
    Hirsova = Cidade('Hirsova',151)
    Iasi = Cidade('Iasi',226)
    Lugoj = Cidade('Lugoj',244)
    Mehadia = Cidade('Mehadia',241)
    Neamt = Cidade('Neamt',234)
    Oradea = Cidade('Oradea',380)
    Pitest = Cidade('Pitest',10)
    Rimnicu_Vilcea = Cidade('Rimnicu Vilcea',193)
    Sibiu = Cidade('Sibiu',253)
    Timisoara = Cidade('Timisoara',329)
    Urziceni = Cidade('Urziceni',80)
    Vaslui = Cidade('Vaslui',199)
    Zerind = Cidade('Zerind',374)
    Bucharest = Cidade('Bucharest',0)

    Arad.addCidadeAdjacente(Adjacente(Zerind,90))
    Arad.addCidadeAdjacente(Adjacente(Sibiu,140))
    Arad.addCidadeAdjacente(Adjacente(Timisoara,118))

    Bucharest.addCidadeAdjacente(Adjacente(Urziceni,85))
    Bucharest.addCidadeAdjacente(Adjacente(Giurgiu,90))
    Bucharest.addCidadeAdjacente(Adjacente(Pitest,101))
    Bucharest.addCidadeAdjacente(Adjacente(Fagaras,211))

    Craiova.addCidadeAdjacente(Adjacente(Dobreta,120))
    Craiova.addCidadeAdjacente(Adjacente(Dobreta,120))
    Craiova.addCidadeAdjacente(Adjacente(Rimnicu_Vilcea,146))

    Dobreta.addCidadeAdjacente(Adjacente(Mehadia,75))
    Dobreta.addCidadeAdjacente(Adjacente(Craiova,120))

    Eforie.addCidadeAdjacente(Adjacente(Hirsova,86))

    Fagaras.addCidadeAdjacente(Adjacente(Sibiu,99))
    Fagaras.addCidadeAdjacente(Adjacente(Bucharest,211))

    Giurgiu.addCidadeAdjacente(Adjacente(Bucharest,90))

    Hirsova.addCidadeAdjacente(Adjacente(Eforie,86))
    Hirsova.addCidadeAdjacente(Adjacente(Urziceni,98))

    Iasi.addCidadeAdjacente(Adjacente(Neamt,87))
    Iasi.addCidadeAdjacente(Adjacente(Vaslui,92))

    Lugoj.addCidadeAdjacente(Adjacente(Timisoara,111))
    Lugoj.addCidadeAdjacente(Adjacente(Mehadia,70))

    Mehadia.addCidadeAdjacente(Adjacente(Lugoj,70))
    Mehadia.addCidadeAdjacente(Adjacente(Dobreta,75))

    Neamt.addCidadeAdjacente(Adjacente(Iasi,87))

    Oradea.addCidadeAdjacente(Adjacente(Zerind,71))
    Oradea.addCidadeAdjacente(Adjacente(Sibiu,151))

    Pitest.addCidadeAdjacente(Adjacente(Rimnicu_Vilcea,97))
    Pitest.addCidadeAdjacente(Adjacente(Bucharest,101))
    Pitest.addCidadeAdjacente(Adjacente(Craiova,138))

    Rimnicu_Vilcea.addCidadeAdjacente(Adjacente(Pitest,97))
    Rimnicu_Vilcea.addCidadeAdjacente(Adjacente(Pitest,80))
    Rimnicu_Vilcea.addCidadeAdjacente(Adjacente(Pitest,146))

    Sibiu.addCidadeAdjacente(Adjacente(Fagaras,99))
    Sibiu.addCidadeAdjacente(Adjacente(Rimnicu_Vilcea,80))
    Sibiu.addCidadeAdjacente(Adjacente(Arad,140))
    Sibiu.addCidadeAdjacente(Adjacente(Oradea,151))

    Timisoara.addCidadeAdjacente(Adjacente(Arad,118))
    Timisoara.addCidadeAdjacente(Adjacente(Lugoj,111))

    Urziceni.addCidadeAdjacente(Adjacente(Vaslui,142))
    Urziceni.addCidadeAdjacente(Adjacente(Hirsova,98))
    Urziceni.addCidadeAdjacente(Adjacente(Bucharest,85))

    Vaslui.addCidadeAdjacente(Adjacente(Iasi,92))
    Vaslui.addCidadeAdjacente(Adjacente(Urziceni,142))

    Zerind.addCidadeAdjacente(Adjacente(Oradea,71))
    Zerind.addCidadeAdjacente(Adjacente(Arad,75))