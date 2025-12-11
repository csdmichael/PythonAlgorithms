from collections import defaultdict

def hasCycle(num_nodes: int, edges: list[list[int]]) -> bool:
   graph = defaultdict(list)
   
   for u, v in edges:
       graph[u].append(v)
       print(f"u={u}, v={v}")

   for key, val in graph.items():
       print(f'Key={key}', val)

   visited = [0] * num_nodes  # 0: unvisited, 1: visiting, 2: visited

   def dfs(node):
       visited[node] = 1  # Mark as visiting

       for neighbor in graph[node]:
           if visited[neighbor] == 1:
               return True  # Cycle detected
           if visited[neighbor] == 0:
               if dfs(neighbor):
                   return True
      
       visited[node] = 2  # Mark as visited
       return False

   for i in range(num_nodes):
       if visited[i] == 0:
           if dfs(i):
               return True
   return False


edges: list[list[int]]
edges = [[1,2],[2,3],[3,1], [1,4]]
y = hasCycle(4, edges)
print(y)