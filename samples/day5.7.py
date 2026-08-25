def dfs(graph,node,visited):
    visited.add(node)
    print(node,end=" ")
    for nei in graph[node]:
        if nei not in visited:
            dfs(graph,nei,visited)
    