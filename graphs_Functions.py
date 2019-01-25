#  Retorna uma lista contendo todas as ligações do grafo no formato (x,y)
def generate_tuples(graph_dict):
    edges = []
    for x in graph_dict:
        for y in graph_dict[x]:
            edges.append((int(x), int(y)))
    return edges


# Retorna a quantidade de vertices e a quantidade de arestas respectivamentes
def return_graph_info(graph_dict):
    return (int(graph_dict.pop('vertices')), int(graph_dict.pop('arestas')))


# Cria um dicionario contendo todas as informações do grafo lidas em um arquivo TXT
def generate_graph_dict(caminho_arquivo):
    with open(caminho_arquivo) as file:
        graph = {line.split()[1]: [] for line in file if line[0] == 'e'}
        file.seek(0)

        for line in file:
            if 'p' == line[0]:
                vertice, arestas = int(line.split()[2]), int(line.split()[3])
                graph['vertices'], graph['arestas'] = vertice, arestas

            if 'e' == line[0]:
                graph[line.split()[1]].append(int(line.split()[2]))

            if 'c' == line[0]:
                continue
    return graph


# param:
#       list_edges: todos as ligações em uma lista de tuplas
#       graph_info: informações sobre o grafo. Sendo respectivamente: (quant_vertices, quant_arestas)
def generate_adjacency_matrix(list_edges, graph_info):
    matrix = []
    # print(list_edges)
    for i in range(int(graph_info[0])):
        line = []
        for j in range(int(graph_info[0])):
            line.append(0)
        matrix.append(line)

    for coord in (list_edges):
        x, y = coord[0] - 1, coord[1] - 1
        matrix[x][y] = 1

    return matrix


#
def generate_fecho_transitivo(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if matrix[i][j] == 1:
                    if matrix[j][i] == 1:
                        if matrix[i][k] != 1:
                            matrix[i][k] = 1
    return matrix


def generate_fecho_antisimetrico(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and matrix[j][i] == 0:
                matrix[j][i] = 1


def return_nos_fontes(matrix):
    sources = []
    for i in range(len(matrix)):
        cont = 0
        for j in range(len(matrix)):
            if matrix[j][i] == 0:
                cont += 1

        if cont == len(matrix):
            sources.append((i, i))

    return sources


# Imprimi a matriz
def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


# Verifica se o grafo é antisimetrico,ou seja: cada par (x,y) existe um (y,x)
# Casp fpr antisimetrico retorna True se não retorna False
def check_antisimetrica(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and matrix[j][i] == 0:
                return False
                break

    return True
