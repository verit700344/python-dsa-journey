def dfs(graph,node,visited):
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(graph,visited,nei)
            