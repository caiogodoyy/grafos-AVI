import uuid
import networkx as nx

import graph
import utils

state = {}
nodes = []

state["isValued"] = int(input("O grafo é valorado?\n[1] Sim\n[0] Não\n>>"))
state["isDirected"] = int(
    input("O grafo é direcionado?\n[1] Sim\n[0] Não\n>>"))
state["insertionType"] = int(
    input("Você deseja inserir tudo de uma vez?\n[1] Sim\n[0] Não\n>>"))

if (state["isDirected"]):
    G = nx.DiGraph()
else:
    G = nx.Graph()

if (state["insertionType"]):
    userInput = utils.parser(str(input(
        "Para montar o seu grafo, forneça todos os vértices, separados por um espaço\n>>")))
    nodes = userInput.split(" ")
    graph.addNodes(G, nodes)

    if (state["isValued"]):
        userInput = utils.parser(str(input(
            "Agora, digite os nomes dos pares de vértices que formam as arestas, seguidos pelo valor da aresta correspondente\nExemplo: A B 10 B C 15\n>>")))
        edges = userInput.split(" ")
        utils.convertEdgeValuesToFloat(edges)
    else:
        userInput = utils.parser(str(input(
            "Agora, digite os nomes dos pares de vértices que formam as arestas\nExemplo: A B B C\n>>")))
        edges = userInput.split(" ")
else:
    while (True):
        op = int(
            input("O que você deseja fazer?\n[0] Finalizar\n[1] Adicionar vértice\n[2] Adicionar aresta\n>>"))

        match op:
            case 0:
                break
            case 1:
                node = utils.parser(
                    str(input("Digite o nome do vértice a ser adicionado\n>>")))
                graph.addNode(G, node)
            case 2:
                if (state["isValued"]):
                    nodes.append(utils.parser(
                        str(input("Digite o nome do primeiro vértice : "))))
                    nodes.append(utils.parser(
                        str(input("Digite o nome do segundo vértice: "))))
                    nodes.append(float(input("Agora, digite o valor da aresta: ")))
                else:
                    nodes.append(utils.parser(
                        str(input("Digite o nome do primeiro vértice: "))))
                    nodes.append(utils.parser(
                        str(input("Digite o nome do segundo vértice: "))))

graph.addEdges(G, edges, state)
print("Grafo construído com sucesso! :)")

sessionId=str(uuid.uuid4())
path=f"images\{sessionId}"
graph.printGraph(G, path)

print("O que você quer fazer com seu grafo?")
op=1
while (op):
    if (state["isValued"] and not state["isDirected"]):
        op=int(input("[0] Sair\n[1] Ver ordem e tamanho\n[2] Ver ligações de um vértice\n[3] Ver grau de um vértice\n[4] Checar adjacência entre vertices\n[5] Encontrar caminho mais curto\n>>"))
    else:
        op=int(input(
            "[0] Sair\n[1] Ver ordem e tamanho\n[2] Ver ligações de um vértice\n[3] Ver grau de um vértice\n[4] Checar adjacência entre vertices\n>>"))

    print("\n")
    if (op == 1):
        print("Ordem: ", G.number_of_nodes())
        print("Tamanho: ", G.number_of_edges())
    if (op == 2):
        node=utils.parser(str(
            input("De qual vértice você quer ver as ligações?\n>>")))
        if (state["isDirected"]):
            if (G.in_edges(node)):
                print(G.in_edges(node))
            if (G.out_edges(node)):
                print(G.out_edges(node))
        else:
            if (G.out_edges(node)):
                print(G.out_edges(node))

    if (op == 3):
        node=utils.parser(str(
            input("De qual vértice você quer ver o grau?\n>>")))
        print(f"O grau do vértice {node} é: {G.degree[node]} ")

    if (op == 4):
        node1=utils.parser(str(input("Digite o primeiro vértice: ")))
        node2=utils.parser(str(input("Digite o segundo vértice: ")))
        if (G.has_edge(node1, node2)):
            print("Sim! Existe a ligação entre esses dois vértices")
        else:
            print("Não... Não existe a ligação entre esses dois vértices")

    if (op == 5 and state["isValued"] and not state["isDirected"]):
        T=nx.minimum_spanning_tree(G)
        graph.printGraph(T, path)
    print("\n")
