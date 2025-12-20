from collections import defaultdict

def hasCycle(numNodes: int, edges: list[list[int]])->bool:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    visited = [0] * numNodes

    # 0: Not visited
    # 1: visiting
    # 2: visited

    def dfs(node) -> bool:
        '''
        Todo:
        Perform depth first search and return false once cycte is found
        '''
        visited[node] = 1
        for neighbor in graph[node]:
            if visited[neighbor] == 1:
                return True
            if visited[neighbor] == 0:
                if dfs(neighbor):
                    return True
        visited[node] = 2
        return False 
    
    for i in range(numNodes):
        if visited[i] == 0:
            if dfs(i):
                return True
    return False
    


