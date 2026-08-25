def has_cycle(graph):
    visited=set()
    def dfs(node,parent):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei,node):
                    return True
            elif parent != nei:

        
                return True
        return False
    for node in graph:
        if node not in visited:
            if dfs(node,-1):
            
                return True
    return False
graph1 = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}
print(has_cycle(graph1))  # False (no cycle)

graph2 = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'A']
}
print(has_cycle(graph2))  # True (cycle A-B-C-D-A)