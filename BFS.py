#Pseudocode for BFS(Breadth First Search) using Queue:-
#1) procedure BFS(G, root) is 
#2)     let Q be a queue
#3)     label root as dicovered
#4)     Q.enqueue(root)
#5)     while Q is not empty do
#6)         v:= Q.dequeue()
#7)         for all edges from v to w in G.adjacentEdges(v) do
#8)             if w is not labelled as discovered then
#9)                 label w as discovered
#10)                Q.enqueue(w), w is the other end of the edge.
#This prohram of BFS is performed after the initialisation of the graphs using class.
def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph.data) #At first, all the nodes are undiscovered or unvisited, therefore, the queue is said to be empty.
    distance = [None] * len(graph.data) #A variable distance is initialised to keep track of the distances(no. of edges) of each nodes to the other, initially it is None for the full length of the graph.data.
    discovered[root] = True #The root element is initialised to True at the beginning.
    queue.append(root) #Value appended at the root.
    distance[root] = 0
    parent = [None] * len(graph.data)
    index = 0 #Python does not supports dequeue operation directly, therefore, initialising an index as 0, and once we dequeue an element, we increase the index count by 1.
    while index < len(queue):
        #dequeue
        current = queue[index]
        index = index+1 #index += 1
        #checking all the adjacent edges of the current node.
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                discovered[node] = True
                queue.append(node)
    return queue, distance, parent
#distance, parent not much needed.
#Time Complexity, T(N) = O(n+2m), n = no. of vertices, m = no. of edges, or O(n+m)