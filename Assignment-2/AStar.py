# Assignment No. 2
# Title: Implementation of A* Algorithm

import heapq

# Graph representation
# Each node contains its neighboring nodes and edge costs
graph = {
    'A': {'B': 2, 'E': 3},
    'B': {'C': 1, 'G': 9},
    'C': {},
    'E': {'D': 6},
    'D': {'G': 1},
    'G': {}
}

# Heuristic values (h(n)) given in the assignment
heuristic = {
    'A': 11,
    'B': 6,
    'C': 99,
    'E': 7,
    'D': 1,
    'G': 0
}


def a_star(graph, heuristic, start, goal):
    # Priority queue stores (f(n), g(n), current_node, path)
    open_list = []

    # Initial cost
    g_cost = 0

    # f(n) = g(n) + h(n)
    f_cost = g_cost + heuristic[start]

    heapq.heappush(open_list, (f_cost, g_cost, start, [start]))

    # Store the best known cost to each node
    best_g = {start: 0}

    while open_list:

        # Select node with the lowest f(n)
        f, g, current, path = heapq.heappop(open_list)

        # If goal is reached, return the path and cost
        if current == goal:
            return path, g

        # Explore neighboring nodes
        for neighbor, cost in graph[current].items():

            new_g = g + cost

            # If a better path to the neighbor is found
            if neighbor not in best_g or new_g < best_g[neighbor]:

                best_g[neighbor] = new_g

                # Calculate f(n)
                new_f = new_g + heuristic[neighbor]

                # Add the neighbor to the priority queue
                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    # If no path exists
    return None, float('inf')


# Starting and goal nodes
start = 'A'
goal = 'G'

# Execute A* algorithm
path, cost = a_star(graph, heuristic, start, goal)

# Display the result
if path:
    print("A* Algorithm")
    print("Start Node:", start)
    print("Goal Node:", goal)
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path exists from", start, "to", goal)
