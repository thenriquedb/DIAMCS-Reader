import graphs_Functions

# def generate_graph_list():
#     graph_dict = []
#     with open('arquivos/graphEDIT.txt') as file:
#         for line in file:
#             line = line.rstrip('\n')  # Remove o caracter de quebra de linha)
#
#             # Informações basicas sobre o grafo
#             if 'p' in line:
#                 graph_dict.append((line[-3], line[-1]))
#
#             # Arestas de ligações
#             if 'e' == line[0]:
#                 graph_dict.append((line[-3], line[-1]))
#
#
#             # Linha de comentario, deve ser desconsiderada
#             elif 'c' in line:
#                 continue
#
#     return graph_dict


if __name__ == '__main__':
    graph_dict = graphs_Functions.generate_graph_dict('arquivos/graph14.txt')
    graph_infos = graphs_Functions.return_graph_info(graph_dict)
    edges = graphs_Functions.generate_tuples(graph_dict)
    matrix = graphs_Functions.generate_adjacency_matrix(edges, graph_infos)
    nos_fontes = graphs_Functions.return_nos_fontes(matrix)

    print("""DADOS DO GRAFO CARREGADO
        Quantidade de vertices: {}
        Quantidade de arestas: {}
        Total nós fontes: {}
    """.format(graph_infos[0], graph_infos[1], len(nos_fontes)))



    # graphs_Functions.generate_fecho_transitivo(matrix)
    # graphs_Functions.generate_fecho_antisimetrico(matrix)
