from collections import defaultdict

def hasCycle(edges: list[list[int]], nodes_count)->bool:
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
    
    visited = [0] * nodes_count

    
    # 0: Not visited
    # 1: visiting
    # 2: Already visited

    def dfs(node)->bool:
        visited[node] = 1 # Visiting

        # Check for cycle
        for neighbor in graph[node]:
            if visited[node] == 1:
                return True
            else:
                if dfs(neighbor) == 1:
                    return True

        visited[node] = 2 # Visited
        return False
    
    for i in range(len(nodes_count)):
        if visited == 0:
            if dfs(i):
                return True
    return False