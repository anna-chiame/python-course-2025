"""
Task 2
Using breadth-first search write an algorithm that can determine
the shortest path from each vertex to every other vertex
(all-pairs shortest path problem).

Important:
- Works for unweighted graphs only.
- Graph is represented as an adjacency list.
"""


# BFS from one vertex


def bfs_shortest_paths(graph, start):
    """
    Perform BFS to find shortest paths from one vertex to all others.

    Args:
        graph: adjacency list (dict)
        start: starting vertex

    Returns:
        Dictionary {vertex: shortest_distance_from_start}
    """
    # Queue for BFS
    queue = []
    # Distance dictionary
    distance = {}

    # Initialize BFS
    queue.append(start)
    distance[start] = 0

    while queue:
        current = queue.pop(0)

        for neighbor in graph.get(current, []):
            # If neighbor is not visited
            if neighbor not in distance:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    return distance



# All-Pairs Shortest Path


def all_pairs_shortest_paths(graph):
    """
    Compute shortest paths between all pairs of vertices
    using BFS.

    Args:
        graph: adjacency list (dict)

    Returns:
        Dictionary of dictionaries:
        {
            v1: {v1: 0, v2: 1, ...},
            v2: {v1: 1, v2: 0, ...},
            ...
        }
    """
    all_distances = {}

    for vertex in graph:
        # Run BFS from each vertex
        all_distances[vertex] = bfs_shortest_paths(graph, vertex)

    return all_distances



# Example usage


graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

result = all_pairs_shortest_paths(graph)

for start in result:
    print("From", start, ":", result[start])