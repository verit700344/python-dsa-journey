from collections import deque


def shortest_path(graph,start):
    visited={start:0}
    queue=deque([start])
    while queue:
        node= queue.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited[nei]=visited[node]+1
                queue.append(nei)
    return visited