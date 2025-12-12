def transpose_graph(graph):
    """
    Build the transpose of a directed graph (reverse all edges).

    Args:
        graph: dict where graph[u] is a list of outgoing neighbors of u.

    Returns:
        A new dict representing the transposed graph.
    """
    gt = {}

    # Ensure all vertices exist in gt (even isolated ones)
    for u in graph:
        if u not in gt:
            gt[u] = []
        for v in graph[u]:
            if v not in gt:
                gt[v] = []

    # Reverse edges
    for u in graph:
        for v in graph[u]:
            gt[v].append(u)

    return gt


def dfs_fill_order(graph, u, visited, order):
    """
    DFS that records vertices by finish time (postorder).

    Args:
        graph: directed graph adjacency list
        u: current vertex
        visited: set of visited vertices
        order: list to append vertices after exploring all descendants
    """
    visited.add(u)

    for v in graph.get(u, []):
        if v not in visited:
            dfs_fill_order(graph, v, visited, order)

    # Push after exploring all neighbors -> finish time order
    order.append(u)


def dfs_collect_component(graph, u, visited, component):
    """
    DFS that collects all reachable vertices into 'component'.

    Args:
        graph: directed graph adjacency list
        u: current vertex
        visited: set of visited vertices
        component: list collecting this SCC vertices
    """
    visited.add(u)
    component.append(u)

    for v in graph.get(u, []):
        if v not in visited:
            dfs_collect_component(graph, v, visited, component)


def strongly_connected_components(graph):
    """
    Compute Strongly Connected Components (SCC) using Kosaraju's algorithm.

    Args:
        graph: dict adjacency list of a directed graph.

    Returns:
        List of SCCs, where each SCC is a list of vertices.
    """
    visited = set()
    order = []

    # 1) DFS on original graph to compute finish order
    # Make sure to include vertices that appear only as neighbors
    all_vertices = set(graph.keys())
    for u in graph:
        for v in graph[u]:
            all_vertices.add(v)

    for u in all_vertices:
        if u not in visited:
            dfs_fill_order(graph, u, visited, order)

    # 2) Transpose the graph
    gt = transpose_graph(graph)

    # 3) DFS on transposed graph in reverse finish order
    visited.clear()
    scc_list = []

    for u in reversed(order):
        if u not in visited:
            component = []
            dfs_collect_component(gt, u, visited, component)
            scc_list.append(component)

    return scc_list



# Example usage

graph = {
    "A": ["B"],
    "B": ["C", "E", "F"],
    "C": ["D", "G"],
    "D": ["C", "H"],
    "E": ["A", "F"],
    "F": ["G"],
    "G": ["F"],
    "H": ["D", "G"],
}

print(strongly_connected_components(graph))
