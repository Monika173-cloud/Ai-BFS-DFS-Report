"""Breadth First Search and Depth First Search on a graph (Unit 1)."""
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

def bfs(graph, start):
    """Visit nodes level by level using a queue (FIFO)."""
    visited, order = {start}, []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
    return order

def dfs(graph, node, visited=None, order=None):
    """Go as deep as possible before backtracking (recursion = stack)."""
    if visited is None:
        visited, order = set(), []
    visited.add(node)
    order.append(node)
    for nb in graph[node]:
        if nb not in visited:
            dfs(graph, nb, visited, order)
    return order

def bfs_path(graph, start, goal):
    """Shortest path (fewest edges) from start to goal using BFS."""
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        if path[-1] == goal:
            return path
        for nb in graph[path[-1]]:
            if nb not in visited:
                visited.add(nb)
                queue.append(path + [nb])
    return None

def dfs_path(graph, start, goal):
    """A path from start to goal found by DFS (not always the shortest)."""
    stack = [[start]]
    visited = set()
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for nb in reversed(graph[node]):
                stack.append(path + [nb])
    return None

if __name__ == "__main__":
    print("Graph (adjacency list):")
    for k, v in graph.items():
        print(" ", k, "->", v)
    print("\nBFS traversal from A :", " -> ".join(bfs(graph, 'A')))
    print("DFS traversal from A :", " -> ".join(dfs(graph, 'A')))
    print("\nBFS path A to F      :", " -> ".join(bfs_path(graph, 'A', 'F')))
    print("DFS path A to F      :", " -> ".join(dfs_path(graph, 'A', 'F')))
