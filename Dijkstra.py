#In the Dijkstra's algorithm, the task is to find the shortest path between the source and the target.
def shortest_path(graph, source, target):
    visited = [False] *len(graph.data) #Initially, no noes are visited, therefore, it is set to False.
    parent = [None] * len(graph.data)
    distance = [float('inf')]*len(graph.data) #Distance is set to infinity from source to all the other nodes.
    queue = [] #all the nodes that gets visited will be inserted in this queue.
    distance[source] = True
    queue.append(source)
    index = 0
    while index < len(queue) and not visited[target]: #This loop works till the index position is less than the elements present in the queue and the target is still not visited.
        current = queue[index]
        visited[current] = True
        index += 1
        #update distances of all the neighbors by a function calling
        update_distances(graph, current, distance, parent)
        #find the first unvisited node from the current node of smaller distance
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)
        visited[current] = True
    return distance[target], parent
def update_distances(graph, current, distance, parent = None):
    #Update the distance of the current node neighbors,
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors): #range function can also be used here in place of enumerate.
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current
def pick_next_node(distance, visited):
    #Pick the next unvisited node at the smallest distance.
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node  
            min_distance = distance[node]
    return min_node
#Time Complexity = O(n*n + m)