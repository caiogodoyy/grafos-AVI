import uuid
import networkx as nx

import graph
import utils

NON_OP = "A opção que você digitou não existe.\n"

state = {}
nodes = []
edges = []

state["isValued"] = utils.getInput(
    "int", "O grafo é valorado?\n[1] Sim\n[0] Não\n>>")
state["isDirected"] = utils.getInput(
    "int", "O grafo é direcionado?\n[1] Sim\n[0] Não\n>>")
state["insertionType"] = utils.getInput(
    "int", "Você deseja inserir tudo de uma vez?\n[1] Sim\n[0] Não\n>>")

if (state["isDirected"]):
    G = nx.DiGraph()
else:
    G = nx.Graph()

if (state["insertionType"]):
    userInput = utils.parser(utils.getInput(
        "str", "Para montar o seu grafo, forneça todos os vértices, separados por um espaço\n>>"))
    nodes = userInput.split(" ")
    graph.addNodes(G, nodes)

    while (True):
        if (state["isValued"]):
            userInput = utils.parser(utils.getInput(
                "str", "Agora, digite os nomes dos pares de vértices que formam as arestas, seguidos pelo valor da aresta correspondente\nExemplo: A B 10 B C 15\n>>"))
            edges = userInput.split(" ")
            if (utils.validateEdges(edges, state) and utils.convertEdgeValuesToFloat(edges)):
                break
        else:
            userInput = utils.parser(utils.getInput(
                "str", "Agora, digite os nomes dos pares de vértices que formam as arestas\nExemplo: A B B C\n>>"))
            edges = userInput.split(" ")
            if (utils.validateEdges(edges, state)):
                break
else:
    while (True):
        op = utils.getInput(
            "int", "O que você deseja fazer?\n[0] Finalizar\n[1] Adicionar vértice\n[2] Adicionar aresta\n>>")

        match op:
            case 0:
                break
            case 1:
                node = utils.parser(utils.getInput(
                    "str", "Digite o nome do vértice a ser adicionado\n>>"))
                graph.addNode(G, node)
            case 2:
                if (state["isValued"]):
                    nodes.append(utils.parser(utils.getInput(
                        "str", "Digite o nome do primeiro vértice: ")))
                    nodes.append(utils.parser(utils.getInput(
                        "str", "Digite o nome do segundo vértice: ")))
                    nodes.append(utils.getInput(
                        "float", "Agora, digite o valor da aresta: "))
                else:
                    nodes.append(utils.parser(utils.getInput(
                        "str", "Digite o nome do primeiro vértice: ")))
                    nodes.append(utils.parser(utils.getInput(
                        "str", "Digite o nome do segundo vértice: ")))
            case _:
                print(NON_OP)

if (edges):
    graph.addEdges(G, edges, state)
print("Grafo construído com sucesso! :)")

sessionId = str(uuid.uuid4())
path = f"Grafos\images\{sessionId}"
graph.printGraph(G, path, 0)

print("O que você quer fazer com seu grafo?")
op = 1
while (op):
    op = utils.getInput(
        "int", "[0] Sair\n[1] Ver ordem e tamanho\n[2] Ver ligações de um vértice\n[3] Ver grau de um vértice\n[4] Checar adjacência entre vertices\n[5] Encontrar caminho mais curto\n>>\n>>")

    print("\n")
    match op:
        case 0:
            break
        case 1:
            print("Ordem: ", G.number_of_nodes())
            print("Tamanho: ", G.number_of_edges())
        case 2:
            node = utils.parser(utils.getInput(
                "str", "De qual vértice você quer ver as ligações?\n>>"))
            if (state["isDirected"]):
                print(G.in_edges(node))
                print(G.out_edges(node))
            else:
                print(G.edges(node))
        case 3:
            node = utils.parser(utils.getInput(
                "str", "De qual vértice você quer ver o grau?\n>>"))
            print(f"O grau do vértice {node} é: {G.degree[node]} ")
        case 4: 
            node1 = utils.parser(utils.getInput(
                "str", "Digite o nome do primeiro vértice: "))
            node2 = utils.parser(utils.getInput(
                "str", "Digite o nome do segundo vértice: "))
            if (G.has_edge(node1, node2) or G.has_edge(node2, node1)):
                print("Sim! Esses dois vértices são adjacentes")
            else:
                print("Não... Esses dois vértices não são adjacentes")
        case 5:
            Fnode1 = utils.parser(utils.getInput(
                "str", "Digite o nome do primeiro vértice: "))
            Fnode2 = utils.parser(utils.getInput(
                "str", "Digite o nome do segundo vértice: "))
            if (nx.has_path(G,Fnode1,Fnode2)):
                if state["isValued"]:
                    T = nx.shortest_path(G, source = Fnode1, target = Fnode2, weight = "weight")
                    Spath = nx.shortest_path_length(G,source = Fnode1, target = Fnode2)
                else:
                    T = nx.shortest_path(G, source = Fnode1, target = Fnode2)
                    Spath = nx.shortest_path_length(G,source = Fnode1, target = Fnode2)
                graph.printGraph(G, path, T)
                print(f"Valor do menor caminho: {Spath}")
            else:
                print(f"Não possui um caminho entre {Fnode1} e {Fnode2}")
        case _:
            print(NON_OP)
    print("\n")