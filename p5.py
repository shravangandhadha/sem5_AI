import heapq

# Graph representation
graph = {
    "Warehouse": [("A", 2), ("B", 4)],
    "A": [("C", 3), ("D", 5)],
    "B": [("E", 2), ("F", 3)],
    "C": [("Customer", 4)],
    "D": [("Customer", 2)],
    "E": [("Customer", 5)],
    "F": [("Customer", 2)],
    "Customer": []
}

# Heuristic values
heuristic = {
    "Warehouse": 6,
    "A": 5,
    "B": 4,
    "C": 4,
    "D": 2,
    "E": 3,
    "F": 2,
    "Customer": 0
}

# A* Search Function
def a_star(start, goal):
    open_list = []

    # (f, g, current_node, path)
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))

    visited = set()

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        if node == goal:
            print("Best Route:", " -> ".join(path))
            print("Total Cost:", g)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    print("No path found!")

# Driver Code
a_star("Warehouse", "Customer")