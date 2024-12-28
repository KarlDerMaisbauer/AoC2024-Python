import networkx as nx

# with open("input-small.txt", 'r') as input_file:
with open("input.txt", 'r') as input_file:
    G = nx.Graph()
    edges = []
    vertices = set()
    for line in input_file:
        parts = line.rstrip().split("-")
        vertices.add(parts[0])
        vertices.add(parts[1])
        edges.append((parts[0], parts[1]))
    G.add_edges_from(edges)
    G.add_nodes_from(list(vertices))

    cliques = list(nx.find_cliques(G))
    largest_clique = max(cliques, key=len)
    largest_clique.sort()
    print(",".join(largest_clique))
