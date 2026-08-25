from collections import deque
def bfs (graph,start):
    visited =set()
    queue = deque ([start])
    visited.add([start])

    while queue:
        node =queue.popleft()
        print(node,end="" )

        for nei in graph[node]:
            if nei not in visited :
                visited.add(nei)
                queue.append(nei)




