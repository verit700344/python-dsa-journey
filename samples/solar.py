def count_components(graph):
    visited=set()
    count=0
    def dfs(node):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)
    for node in graph:
        if node not in visited:
            dfs(node)
            count+=1
    return count
graph={
    1:[2,3],2:[3,6],3:[4,7]


}
print(dfs(graph,1))