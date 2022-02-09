from modules.grafo import Grafo
import modules.algoritmos as algoritmos

def main():
    # caminho_arquivo = input("Insira o caminho pro arquivo que contem o grafo:\n>")
    grafo = Grafo("grafo.txt")
    # algoritmos.busca_em_largura(grafo, 1)
    # algoritmos.dijkstra(grafo, 1)
    print(algoritmos.busca_em_profundidade({}, grafo, 1, [0]))

if __name__ == "__main__":
    main()