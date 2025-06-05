graph = {    
'A': ['S', 'B'], 
'B': ['S'], 
'S': ['C', 'G'], 
'C': ['E', 'D', 'H', 'F'], 
'G': ['H', 'F', 'C'], 
'E': [], 
'D': [], 
'H': [], 
'F': [],
}

def bfs(startNode):
    q = [startNode]
    v = set()
    while q:
        n = q.pop(0)
        if n not in v:
            print(n)
            v.add(n)
            for x in graph[n]:
               q.append(x) 
               
print("bfs")
bfs("A")

def dfs(startNode,destNode,v):
    if startNode not in v:
        print(startNode)
        v.add(startNode)
        for x in graph[startNode]:
            dfs(x,destNode,v)

print("\n\n\ndfs")
dfs("A","F",set())
