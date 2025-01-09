def build_graph():
    return {
        1: [2],
        2: [1, 5],
        3: [6],
        4: [6, 7],
        5: [2],
        6: [3, 4, 7],
        7: [4, 6],
    }

def path_exists(graph, start, target):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node == target:
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append(neighbor)
    return False

if __name__ == "__main__":
    g = build_graph()
    start_node = int(input("Enter the start node: "))
    end_node = int(input("Enter the end node: "))
    
    if path_exists(g, start_node, end_node):
        print("True – a path exists!")
    else:
        print("False – no path found.")