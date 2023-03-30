import matplotlib.pyplot as plt
import networkx as nx


def printGraph(G, path):
    print("\n")
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color="lightblue")
    nx.draw_networkx_edges(G, pos, edge_color="grey")
    nx.draw_networkx_labels(G, pos)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.axis("off")
    plt.savefig(path)
    plt.show()
    print("\n")

def buildGraph(G, nodes, state):
    if (state["isValued"]):
        for i in range(0, len(nodes)-1, 3):
            G.add_node(nodes[i])
            G.add_node(nodes[i+1])
            G.add_edge(nodes[i], nodes[i+1], weight=nodes[i+2])
    else:
        for i in range(0, len(nodes)-1, 2):
            G.add_node(nodes[i])
            G.add_node(nodes[i+1])
            G.add_edge(nodes[i], nodes[i+1])
