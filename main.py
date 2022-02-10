from modules.grafo import Grafo
import modules.algoritmos as algoritmos

def main():
    caminho_arquivo = input("Insira o caminho pro arquivo que contem o grafo:\n>")
    grafo = Grafo(caminho_arquivo)
    # algoritmos.componentes_fortemente_conexas(grafo)
    # algoritmos.ordenacao_topologica(grafo)

if __name__ == "__main__":
    main()