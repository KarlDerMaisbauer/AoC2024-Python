
def find_triple(val, edges):
    triples = []
    canidates = []
    for edge in edges:
        if val in edge:
            # print(f"it edges {val}, {edge}")
            canidates.extend(list(edge.difference(frozenset([val]))))
    # print(canidates)
    for i in range(len(canidates)):
        for k in range(i+1, len(canidates), 1):
            edge1 = frozenset([canidates[i], canidates[k]])
            if edge1 in edges:
                triples.append((val, canidates[i], canidates[k]))
    return triples


def clean_edges(triples, edges):
    # print(triples)
    for triple in triples:
        # print(triple)
        edges = set(filter(
            lambda x: not triple[0] in x, edges))
    return edges


# with open("input-small.txt", 'r') as input_file:
with open("input.txt", 'r') as input_file:
    edges = set()
    vertices = set()
    for line in input_file:
        parts = line.rstrip().split("-")
        vertices.add(parts[0])
        vertices.add(parts[1])
        edges.add(frozenset(parts))

    result_triples = []
    for vertex in vertices:
        if not vertex.startswith('t'):
            continue
        triples = find_triple(vertex, edges)
        edges = clean_edges(triples, edges)
        result_triples.extend(triples)
    # print(result_triples)
    print(len(result_triples))

    # print(vertices)
    # print(edges)


#    258330 too high
