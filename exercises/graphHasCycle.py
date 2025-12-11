from collections import defaultdict

def hasCycle(node_count: int, edges: list[list[int]])->bool:
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
    
    visited = [0] * node_count

    # 0: Not visited
    # 1: visiting
    # 2: Already visited

    def dfs(node) -> bool:
        visited[node] = 1 # visiting

        for neighbor in graph[node]:
            if visited[neighbor] == 1:
                return True # Cycle found
            if visited[neighbor] == 0:
                if dfs(neighbor) == 1:
                    return True # Cycle found
        
        visited[node] = 2 # Mark Node as Visited
        return False
    
    for i in range(node_count):
        if visited[i] == 0:
            if dfs(i):
                return True
    return False