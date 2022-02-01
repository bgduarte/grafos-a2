class Grafo:
    def __init__(self, arquivo):
        # Como o indice dos vertices começa em 1, colocamos null na posição 0 das seguintes listas
        self.__rotulos = [None] # Lista de rotulos
        self.__listaDeAdj = [[None]] # para cada vertice há uma lista de vizinhos
        self.__listaDePesos = [[None]] # igual a lista adjacencia, mas com os pesos das arestas
        self.__arestas = []

        self.__ler(arquivo)
        
    
    # carregar um grafo a partir de um arquivo no formato especificado
    def __ler(self, caminho_arquivo): #recebe o nome do arquivo
        with open(caminho_arquivo, 'r') as arquivo:
            num_vertices = int(arquivo.readline().split(' ')[1])
            for i in range(num_vertices):
                self.__rotulos.append(arquivo.readline().split(' ')[1])
                self.__listaDeAdj.append([])
                self.__listaDePesos.append([])
            
            arquivo.readline() # le "*edges"
            for linha in arquivo:
                secoes = linha.split(' ')
                indice = int(secoes[0])
                vertice = int(secoes[1])
                peso = float(secoes[2])

                self.__listaDeAdj[indice].append(vertice)
                self.__listaDePesos[indice].append(peso)
                self.__arestas.append((indice, vertice, peso))

    # Retorna quantidade de vertices
    def qtdVertices(self):
        return len(self.__rotulos)-1
    
    # Retorna a quantidade de arestas
    def qtdArestas(self):
        return len(self.__arestas)

    # Retorna o grau do vertice v
    def grau(self, v):
        return len(self.__listaDeAdj[v])
    
    # Retorna o rotulo do vertice v
    def rotulo(self, v):
        return self.__rotulos[v]
    
    # Retorna os vizinhos do vertice v
    def vizinhos(self, v):
        return self.__listaDeAdj[v]
    
    # Retorna True se os dois vertices estiverem ligados por uma aresta
    def haAresta(self, u, v):
        for vizinho in self.__listaDeAdj[u]:
            if(vizinho == v):
                return True
        return False

    # se {u, v} pertence à E, retorna o peso da aresta {u,v}; 
    # se não existir, retorna um valor  infinito positvo(maior ponto flutuante)
    def peso(self, u, v):
        if self.haAresta(u,v):
            for i in range(len(self.__listaDeAdj[u])):
                if self.__listaDeAdj[u][i] == v:
                    return self.__listaDePesos[u][i]
        else:
            return float('inf')