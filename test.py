def traverse_graph(graph, start_point, visited):
    visited.add(start_point)
    for neighbor in graph[start_point]:
        if neighbor not in visited:
            traverse_graph(graph, neighbor, visited)

def find_connected_data(data, target1):
    graph = {}
    for d in data:
        source, target, _ = d['source'], d['target'], d['type']
        if source not in graph:
            graph[source] = []
        graph[source].append(target)
        if target not in graph:
            graph[target] = []
        graph[target].append(source)


    visited = set()
    traverse_graph(graph, target1, visited)

    return visited


data = [
    {"source": "192.168.1.3-192.168.1.1", "target": "192.168.1.1-192.168.1.2", "type": 1},
    {"source": "192.168.1.1-192.168.1.2", "target": "192.168.1.2-192.168.1.3", "type": 2},
    {"source": "192.168.1.2-192.168.1.3", "target": "192.168.1.3-192.168.1.1", "type": 3},
    {"source": "192.168.1.1-192.168.1.2", "target": "192.168.1.2-192.168.1.4", "type": 4},
    {"source": "192.168.1.2-192.168.1.4", "target": "192.168.1.4-192.168.1.1", "type": 5},
    {"source": "192.168.1.4-192.168.1.1", "target": "192.168.1.1-192.168.1.2", "type": 7},
    {"source": "192.168.1.2-192.168.1.4", "target": "192.168.1.4-192.168.1.2", "type": 8},
    {"source": "192.168.1.4-192.168.1.2", "target": "192.168.1.2-192.168.1.3", "type": 9},

    {"source": "192.168.1.11-192.168.1.12", "target": "192.168.1.12-192.168.1.14", "type": 14},
    {"source": "192.168.1.12-192.168.1.14", "target": "192.168.1.14-192.168.1.11", "type": 15},
    {"source": "192.168.1.14-192.168.1.11", "target": "192.168.1.11-192.168.1.12", "type": 16},
    {"source": "192.168.1.12-192.168.1.14", "target": "192.168.1.14-192.168.1.12", "type": 17},
    {"source": "192.168.1.14-192.168.1.12", "target": "192.168.1.12-192.168.1.13", "type": 18},
    {"source": "192.168.1.15-192.168.1.12", "target": "192.168.1.12-192.168.1.13", "type": 20},
    {"source": "192.168.1.10-192.168.1.11", "target": "192.168.1.11-192.168.1.12", "type": 19}

]
#
# print(find_connected_data(data, "192.168.1.12-192.168.1.14"))
