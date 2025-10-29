class graph_Matrix :
    def __init__(self ) :
        self.graph = []
        self.node = []
        self.node_count = 0
    
    def add_node(self, v):
        if v in self.node:
            print('value already found on Graph')
        self.node_count += 1
        self.node.append(v)
        for row in self.graph:
            row.append(0)
        self.graph.append([0] * self.node_count)

    def print_graph(self):
        for i in range(self.node_count):
            for j in range(self.node_count):
                print(format(self.graph[i][j],"<3"),end=" ")
            print()

    def add_edge(self, v1, v2):
        if v1 not in self.node :
            print(v1 , 'value not present inside the graph')
        elif v2 not in self.node :
            print(v2, 'is not present in graph')

        else :
            index1 = self.node.index(v1)
            index2 = self.node.index(v2)

            if self.graph[index1][index2] == 0 :
                
                self.graph[index1][index2] = 1
                self.graph[index2][index1] = 1
                
            else :
                print(f'{v1} and {v2} is already connectedd')
                
    def add_directed_edge(self, d1, d2, cost):
        if d1 not in self.node :
            print(d1, 'is not found on this graph')
            
        elif d2 not in self.node :
            print(d2,'is not found on this graph')
            
        else:
            index1 = self.node.index(d1)
            index2 = self.node.index(d2)

            self.graph[index1][index2] = cost

    def __str__(self):
        return str(self.node)

# G = graph_Matrix()
# G.add_node('A')
# G.add_node('B')
# G.add_node('C')
# # G.add_node('D')
# G.add_edge('D','C')
# # G.add_edge('D','A')
# G.print_graph()
# print(G.graph)

from collections import deque

class Adjecency_list :
    def __init__(self):
        self.graph = {}

    def add_vertex(self,v):
        if v in self.graph :
            print(v,'is already in graph')
        else :
            self.graph[v] = []

    def __str__(self):
        return str(self.graph)
    
    # wighted and undirected graph

    def add_edge(self, v1, v2, weight) :
        if v1 not in self.graph :
            print(v1 ,'not found')

        elif v2 not in self.graph:
            print(v2 , 'is not in graph')

        else :
            self.graph[v1].append((v2 , weight))
            self.graph[v2].append((v1,weight))

    # unwighted and directed add edge operations
    def add_directed_edge(self,v1 , v2):
        if v1 not in self.graph :
            print(f'{v1} is not found on this')

        elif v2 not in self.graph :
            print(f'no {v2} value on this graph')

        else :
            self.graph[v1].append(v2)

    def delete_edge(self,v1):
        if v1 not in self.graph:
            print(v1 , 'not found')

        else :
            self.graph.pop(v1)            
            for v in self.graph.values() :
                if v1 in v :
                    v.remove(v1)
                    
                    

    def delete_weighted(self , v) :
        if v not in self.graph :
            print(f'{v} is not found in graph')
        else :
            self.graph.pop(v)
            for i in self.graph :
                li = self.graph[i]
                for j in li :
                    if v in j:
                        li.remove(j)
                        
    def print_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")

    def DFS(self, start , visited=set()):
        if start not in visited :
            visited.add(start)
            print(start , end=', ')
            for child in self.graph[start] :
                self.DFS(child,visited)

    def DFSIterative(self,node) :
        visited = set()
        if node not in self.graph :
            print(node,'is not found on graph')
            return

        stack = [node]  
        while stack :
            current = stack.pop()
            if current not in visited :
                print(current , end=",")
                visited.add(current)
                for i in self.graph[current]:
                    if isinstance(i , tuple):
                        i = i[0]
                    if i not in visited:    
                        stack.append(i)

    def bfs(self ,start):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node , end=",")
                visited.add(node)
                
                for neighbor in self.graph.get(node,[]):
                    if isinstance(neighbor ,tuple) :
                        neighbor = neighbor[0]
                        
                    if neighbor not in visited :    
                        queue.append(neighbor)
                        
    def is_cyclic(self,graph):
        visited = set()
        recStack = set()

        def dfs(node):
            # If node is already in current path → cycle detected
            if node in recStack:
                return True
            # If already visited fully → no need to check again
            if node in visited:
                return False

            # Mark node in current path
            recStack.add(node)
            for neighbor in graph[node]:
                if dfs(neighbor):   # If cycle found in neighbor
                    return True
            # Done exploring this node → remove from path and mark visited
            recStack.remove(node)
            visited.add(node)
            return False

        # Run DFS from every unvisited node
        for node in graph:
            if node not in visited:
                if dfs(node):
                    return True
        return False
    
    def shortest_path(self,  start , end):
        
        visited = set()
        parent = {start:None}
        q = deque([start])

        while q :
            curr = q.popleft()
            if curr == end :
                break
            for neighbor in self.graph[curr]:
                if neighbor not in visited:
                    parent[neighbor] = curr
                    visited.add(neighbor)
                    q.append(neighbor)
        path = []
        if end not in parent:
            return None
        curr = end
        while curr is not None :
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        return path
            

Al = Adjecency_list()
Al.add_vertex('A')
Al.add_vertex('B')
Al.add_vertex('C')
Al.add_vertex('D')
Al.add_vertex('E')
Al.add_directed_edge('A','B')
Al.add_directed_edge('A','C')
Al.add_directed_edge('C','D')
Al.add_directed_edge('D','E')
Al.add_directed_edge('E','C')
print(Al.graph)
res = Al.shortest_path('A','E')
print(res)