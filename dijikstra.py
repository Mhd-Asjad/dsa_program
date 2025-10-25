import heapq

# This is your data defined as an adjacency list
# Format: { node: [(neighbor, cost), ...] }
graph = {

    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5)],
    'C': [('B', 1), ('D', 8)],
    'D': [('E', 3)],
    'E': []  # E is a node, but has no outgoing edges
    
}

start_node = 'A'


def shortest_path(graph, start, end):
    visited = set()
    min_heap = [(0, start)]  # (cost, node)]
    parent = {start: None}
    costs = {start: 0}

    while min_heap:
        current_cost, current_node = heapq.heappop(min_heap)
        print(f"Visiting node {current_node} with current cost {current_cost}")

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == end:
            break

        for neighbor, edge_cost in graph[current_node]:
            if neighbor in visited:
                continue
            new_cost = current_cost + edge_cost
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parent[neighbor] = current_node
                heapq.heappush(min_heap, (new_cost, neighbor))

    path = []
    if end not in parent:
        return None, float('inf')
    curr = end
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path, costs[end]
end_node = 'E'
path, cost = shortest_path(graph, start_node, end_node)
print(f"Shortest path from {start_node} to {end_node}: {path} with cost {cost}")
    
