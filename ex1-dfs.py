class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def dfs(self, src, dsc, visited = set()):
        visited.add(src)
        if src == dsc:
            return [src]
        
        for neighbor in self.graph[src]:
            if neighbor not in visited:
                path = self.dfs(neighbor, dsc, visited)
                if path:
                    return [src] + path
            return []

    def bfs_with_expansion(self, src, dsc):
        visited = set()
        queue = [[src]]
        expansion_process = []
        
        if src == dsc:
            return [src]
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            if node not in visited:
                neighbors = self.graph[node]
                expansion_process.append((node, neighbors))
                
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    
                    if neighbor == dsc:
                        self.print_expansion(expansion_process)
                        return new_path
                
                visited.add(node)
        
        self.print_expansion(expansion_process)
        return []

    def print_expansion(self, expansion_process):
        print("Expand Node | Fringe")
        print("-" * 25)
        for node, fringe in expansion_process:
            print(f"{node}\t\t| {', '.join(map(str, fringe))}")
        print("-" * 25)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    src = 1
    dsc = 3
    path_dfs = g.dfs(src, dsc)
    print(f"DFS Path from {src} to {dsc}: {path_dfs}")

    path_bfs_expansion = g.bfs_with_expansion(src, dsc)
    print(f"BFS Path with expansion from {src} to {dsc}: {path_bfs_expansion}")


