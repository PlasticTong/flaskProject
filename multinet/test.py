def traverse_graph(graph, start_point, visited,res):
    visited.add(start_point)
    for neighbor, edge_type,id in graph[start_point]:
        if neighbor not in visited:
            for neighbor1, edge_type1,id1 in graph[neighbor]:
                # print(id)
                res.append(id1)

            # print(graph[neighbor])
            # res.append(id)
            traverse_graph(graph, neighbor, visited,res)

            # print(id)

def find_connected_data(data, target1):
    graph = {}
    for d in data:
        print(d)
        source, target, edge_type,id = d['source']['name'], d['target']['name'], 1,d['id']
        if source not in graph:
            graph[source] = []
        graph[source].append((target, edge_type,id))
        if target not in graph:
            graph[target] = []
        graph[target].append((source, edge_type,id))

    visited = set()
    res = []
    traverse_graph(graph, target1, visited,res)
    print(graph)

    return res

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

# print(find_connected_data(data, "192.168.1.3-192.168.1.1"))
