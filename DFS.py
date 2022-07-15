#Psuedocode for DFS(Depth First Search):-
#1)procedure DFS_iterative(G, v) is
#2)     let S be a stack
#3)     S.push(v)
#4)     while S is not empty do
#5)         v = S.pop()
#6)         if v is not labelled as discovered then
#7)             label v as discovered
#8)             for all edges from v to w in G.adjacentEdges(v) do
#9)                 S.push(w)
def dfs(graph, root):
    stack = []
    discovered = [False] * len(graph.data)
    result = []
    stack.append(root)
    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append[current]
            for node in graph.data: #adjacent nodes
                if not discovered[node]:
                    stack.append(node)
    return result


#A program for weighted and directed graphs.
class Graph:
    def __init__(self, num_nodes, edges, weighted = False, directed = False): #At the very first, the graph is supposed to be indirected(no direction) and with no weights, therefore initialised as False.
        self.num_nodes = num_nodes
        self.weighted = weighted
        self.directed = directed
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted: #If the edge contains weight
                node1, node2, weight = edge #The edge should contain both the nodes along with the weight, as (1, 2, 3), where 1 and 2 are connected nodes with weight 3 on them.
                self.data[node1].append[node2]
                self.weight[node1].append[weight]
                if not directed:
                    self.data[node2].append[node1]
                    self.weight[node2].weight[node1]
            else:
                node1, node2 = edge
                self.data[node1].append[node2]
                if not directed:
                    self.data[node2].append[node1]
#Time Complexity, T(N) = O(n+2m), n = no. of vertices, m = no. of edges, or O(n+m)