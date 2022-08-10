#At the very first, a class for the graphs must be created with two parameters, num_nodes and edges, where edges is the empty list of pairs in which pairs of the edges betrween the nodes are added. Graphs are represented in the adjacency list in which the list contains the node and contains all the adjacency notes as in the edges.
#Notre that the empty list of pairs, say for 10 elements must be created like :-
# l1 = [[] for _ in range(10)], (note that underscore[_] is used at the place of avvariablre which is not used further in the program, which will create an empty list of lusts of ten elements, like :-
#[[], [], [], [], [], [], [], [], [], []]
#In the following list of lists, if we want to add an element at position 0, then it can simply be done by append function, like :-
#l1[0].append[1]
#The empty list of lists muust not be created like :-
#l1 = [[]] * 10
#In the upper created list of lists, it will also create an empty list of lists, but in this if we want to add an element at any position, that element will be added to all the elements.
#Definining graph:-
class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges: #This will print all the edges of the graph, if print statement is used.
            #Insert into the right lists
            self.data[n1].append[n2] #This will append the node n2 in n1, for example, say n1 = 1, and it is having an edge from 1 to 2, so the other node is n2, i.e., 2, therefore, appending it with n1 as (1, 2).
            self.data[n2].append[n1]
        #To make this graph look as a graphical representation, enumerate() function inside __repr__ function is used.
        #Use of enumerate:-
        #for i, value in enumerate(5, 4, 3, 2):
        #   print(i, value), This will print value of list numbers along with their indices, like:-
        #(0 5), (1, 4), (2, 3), (3, 2)
    def __repr__(self):
        return "\n".join(["{}:{}".format(n, neighnors) for n, neighbors in enumerate(self.data)])
    def __str__(self):
        return self.__repr__()

#Graphs can also be represented using Adjacency Matrix. 
