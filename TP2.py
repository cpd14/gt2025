class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.V = len(matrix)
        
    def get_transpose(self):
        transpose = [[0] * self.V for _ in range(self.V)]
        for i in range(self.V):
            for j in range(self.V):
                transpose[i][j] = self.matrix[j][i]
        return transpose
    
    def get_undirected(self):
        undirected = [[0] * self.V for _ in range(self.V)]
        for i in range(self.V):
            for j in range(self.V):
                undirected[i][j] = max(self.matrix[i][j], self.matrix[j][i])
        return undirected
    
    def dfs_fill_order(self, v, visited, stack):
        visited[v] = True
        for i in range(self.V):
            if self.matrix[v][i] and not visited[i]:
                self.dfs_fill_order(i, visited, stack)
        stack.append(v)
    
    def dfs(self, v, visited, graph):
        visited[v] = True
        for i in range(self.V):
            if graph[v][i] and not visited[i]:
                self.dfs(i, visited, graph)
    
    def get_strongly_connected_components(self):
        stack = []
        visited = [False] * self.V
        
        for i in range(self.V):
            if not visited[i]:
                self.dfs_fill_order(i, visited, stack)
        
        transpose = self.get_transpose()

        visited = [False] * self.V

        scc_count = 0
        while stack:
            v = stack.pop()
            if not visited[v]:
                self.dfs(v, visited, transpose)
                scc_count += 1
        
        return scc_count
    
    def get_weakly_connected_components(self):
        undirected = self.get_undirected()

        visited = [False] * self.V
        wcc_count = 0
        
        for v in range(self.V):
            if not visited[v]:
                self.dfs(v, visited, undirected)
                wcc_count += 1
        
        return wcc_count

if __name__ == "__main__":
    G = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    graph = Graph(G)
    wcc = graph.get_weakly_connected_components()
    scc = graph.get_strongly_connected_components()
    
    print(f"Weakly connected components: {wcc}")
    print(f"Strongly connected components: {scc}")