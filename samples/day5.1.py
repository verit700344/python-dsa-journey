def build_graph(edges):
    graph ={}
    for u,v in edges:
        if u not in graph:
            graph[u]=[]
        if v not in graph:
            graph[v] =[]
        graph[u].append(v)
        graph[v].append(u)
    return graph
edges=[(1,2),(2,4),(3,4)]
print(build_graph(edges))
