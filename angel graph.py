# Struktur Data Graph

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

print("Graph:")

for node in graph:
    print(node, "terhubung dengan", graph[node])