from audioop import reverse
from typing import Dict, List
from .grafo import Grafo

def componentes_fortemente_conexas(grafo: Grafo):
    def ordena_visitados_por_f(visitados: dict):
        visitados = dict(sorted(visitados.items(), key=lambda i: i[1][1], reverse=True))
        return visitados

    visitados = {}
    for v in range(1, grafo.qtdVertices()+1):
        if v not in visitados:
            resultado1 = busca_em_profundidade(visitados, grafo, v, [1])
    
    resultado1 = ordena_visitados_por_f(resultado1)

    transposto = grafo.transposto()

    cFortConexos = []
    visitados = {}
    for v in resultado1:
        antigosVisitados = visitados.copy()
        busca_em_profundidade(visitados, transposto, v, [1])
        cFortConexos.append([k for k in visitados if k not in antigosVisitados])

    cFortConexos = [c for c in cFortConexos if c]

    for c in cFortConexos:
        print(str(c)[1:-1])
    
def ordenacao_topologica(grafo: Grafo):
    def busca_em_profundidade_OT(visitados: dict, grafo: Grafo, vertice, tempo: list, o: list):
        if vertice not in visitados:
            visitados[vertice] = [tempo[0]]
            tempo[0] += 1
            
            for vizinho in grafo.vizinhos(vertice):
                busca_em_profundidade_OT(visitados, grafo, vizinho, tempo, o)

            visitados[vertice].append(tempo[0])
            o.insert(0, vertice)
            tempo[0] += 1
    o = []
    visitados = {}
    tempo = [1]
    for v in range(1, grafo.qtdVertices()+1):
        if v not in visitados:
            busca_em_profundidade_OT(visitados, grafo, v, tempo, o)
    
    # Exibe o resultado no formato da questao
    texto = ''
    for i in range(len(o)):
        texto += str(o[i])
        if i != len(o)-1:
            texto += ' -> '

    print(texto)
        
def busca_em_profundidade(visitados: dict, grafo: Grafo, vertice, tempo: list):
    if vertice not in visitados:
        visitados[vertice] = [tempo[0]]
        tempo[0] += 1
        
        for vizinho in grafo.vizinhos(vertice):
            busca_em_profundidade(visitados, grafo, vizinho, tempo)
        
        visitados[vertice].append(tempo[0])
        tempo[0] += 1

    return visitados