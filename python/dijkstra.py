from collections import defaultdict
from heapq import *


def dijkstra(edges, start, target):
    graph = defaultdict(list)
    for left, right, cost in edges:
        graph[left].append((cost, right))
    queue, visited = [], set()
    heappush(queue, (0, start, start))
    while queue:
        cost, node, path = heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == target:
                return cost, path
            for next_cost, next_node in graph[node]:
                if next_node not in visited:
                    heappush(queue, (cost + next_cost, next_node, path + next_node))


if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    print "=== Dijkstra ==="
    print edges
    print "A -> E:"
    print dijkstra(edges, "A", "E")

    # print "A -> G:"
    # print dijkstra(edges, "A", "G")
    # print "F -> G:"
    # print dijkstra(edges, "F", "G")