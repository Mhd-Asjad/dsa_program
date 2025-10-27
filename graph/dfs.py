class DFS:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}
        
    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)
        
    def visit(self, node):
        if node in self.visited:
            return
        self.visited.add(node)
        for next_node in self.graph[node] :
            self.visit(next_node)

    def dfs(self, start_node) :
        self.visited = set()
        self.visit(start_node)
        return self.visited

    def display(self):
        print("Adjacency list:")
        for node in self.nodes:
            neighbors = ", ".join(str(n) for n in sorted(self.graph.get(node, [])))
            print(f"{node}: {neighbors}")



d = DFS([1, 2, 3, 4, 5])
d.add_edge(1, 2)
d.add_edge(1, 3)
d.add_edge(1, 4)
d.add_edge(2, 4)
d.add_edge(2, 5)
d.add_edge(3, 4)
d.add_edge(4, 5)
d.display()
print()
print(d.dfs(3))