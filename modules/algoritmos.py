from typing import List
from .grafo import Grafo

def componentes_fortemente_conexas(grafo: Grafo):
    resultado1 = busca_em_profundidade({}, grafo, 1, [0])
    transposto = grafo.transposto()
    # fazer um modificado???
    resultado2 = busca_em_profundidade({}, transposto, 1, [0])


def busca_em_profundidade(visitados: dict, grafo: Grafo, vertice, tempo: list):
    if vertice not in visitados:
        visitados[vertice] = [tempo[0]]
        tempo[0] += 1
        
        for vizinho in grafo.vizinhos(vertice):
            busca_em_profundidade(visitados, grafo, vizinho, tempo)
        
        visitados[vertice].append(tempo[0])
        tempo[0] += 1

    return visitados

def busca_em_largura(grafo: Grafo, s: int):
    fila = [s]
    visitados = []
    distanciaAte = dict()
    distanciaAte[s] = 0

    while fila:
        v = fila.pop(0)
        if v not in visitados:
            visitados.append(v)
            for vizinho in grafo.vizinhos(v):
                if vizinho not in visitados:
                    fila.append(vizinho)
                    distanciaAte[vizinho] = distanciaAte[v] + 1
    
    # Exibe o resultado no formato da questao
    texto = '0: '
    indice = 0
    for vertice in distanciaAte:
        if indice != distanciaAte[vertice]:
            texto = texto[:-2]
            indice = distanciaAte[vertice]
            texto += '\n' + str(indice) + ': '
        texto = texto + str(vertice) + ', '
    print(texto)


def dijkstra(grafo: Grafo, s: int):
    def min_dist(dists, visitados):
        local_dists = dists
        min_index = None
        while not min_index:
            min_index = local_dists.index(min(local_dists))
            if min_index not in visitados:
                return min_index
            local_dists.pop(min_index)

    n_vertices = grafo.qtdVertices()
    dists = [float('inf')] * (n_vertices+1)
    dists[s] = 0
    caminho_percorrido = [[]] * (n_vertices+1)
    caminho_percorrido[s] = [s]
    visitados = []
    while len(visitados) != n_vertices:
        v = min_dist(dists, visitados)
        print(v)
        visitados.append(v)
        for z in grafo.vizinhos(v):
            if dists[z] > dists[v] + grafo.peso(v,z):
                dists[z] = dists[v] + grafo.peso(v,z)
                caminho_percorrido[z] = caminho_percorrido[z] + [v]
        print("dists", dists)
        print("caminho percorrido", caminho_percorrido)
        print("visitados", visitados)


    # printar resposta
    for v in range(1, len(dists)):
            print(str(v) + ": " + str(caminho_percorrido[v])[1:-1] + "; d=" + str(dists[v]))    