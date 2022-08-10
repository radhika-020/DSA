#Given a problem, we need to insert, find, update, and list all the list of the usernames. Given condition is, For eg, Radhika must be inserted before Ranjana, in an alphabetical order.
class UserDatabase:
    def __init__(self):
        self.users = [] #an empty list is created for the insertion of the users.
    def insert(self, user):
        i = 0 #for arranging in alphabetical order
        while i < len(self.users):
            if self.users[i].username > user.username: #which means that the inserting user, i.e., the users, if it is greater in alphabetical order of the already existing user,
                break # then, we will not insert here and simply break the loop
            i = i + 1 #and increment i
        self.users.insert(i, user) #if the above condition exceeds, then again the insert function is called for the another user(recursive call).

    def find(self, username):
        for user in self.users: #iterating over the full list of users, to find a user named username, which is the input of the function.
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username) #first, we need to find the user with a certain(given) username, and then we will be updating it, therefore, find function is called here with a certain username of the user.
        target.name, target.email = user.name, user.email

    def list_all(self): #to list all the users in ascending order
        return self.users


#Creating a simple binary tree(note that it is not a binary search tree{bst}).
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None #or, def __init__(key, left = None, right, None):

node0 = TreeNode(3)
node1 = TreeNode(4)
node1 = TreeNode(5) # will create a tree with three nodes, key(root element) = 3, left child = 3, right child = 5
#one more way of adding values to the left and right child can be
#node0.left = TreeNode(4), or node1
#node0.right = TreeNode(5), or node2
#if we connect a variable tree to the node0, then
#tree.key = 3
#tree.left.key = 4
#tree,right.key = 5


#For example, a Binary tree is given with values, 
#tree_tuple = ((1, 3, None)[index = 0], 2[index = 1], ((None, 3, 4), 5, (6, 7, 8))[index = 2])
#here in the above example, 2 is the root node, (1, 3, None) is the left child of the root node, with 3 as the root node,  1 as the left child of 3 and right child of 3 is None.
#Similarly, for other right children, in which 5 is the right child of 2, and so on.
#Code for this can be written as:-
def parse_tuple(data):
    if isinstance(data, tuple) and len(data)==3: #first condition checks if the data is of type tuple and the length of the data is 3, i.e., left, root, and right child(length of data =3).
        node = TreeNode(data[1]) #inserting key of root at position, here 1 is the index number.
        node.left = parse_tuple(data[0]) #calling parse_tuple again because in the above example of tree_tuple, we can see that the left node is itself a tuple and right node is itself a tuple. Here, this is a recursive call.
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


#Inorder traversal(left, root, right)
def traverse_inorder(node):
    if node is None:
        return []
    else:
         return [traverse_inorder(node.left) + [node.key] + traverse_inorder(node.right)] #recursive call

#Preorder traversal(root, left, right)
def traverse_preorder(node):
    if node is None:
        return []
    else:
        return [[node.key] + traverse_inorder(node.left) + traverse_inorder(node.right)]

#Postorder traversal(left, right, root)
def traverse_postorder(node):
    if node is None:
        return []
    else:
        return [traverse_inorder(node.left) + traverse_inorder(node.right) + [node.key]]

#A function to calculate the height of a binary tree(mo of nodes in a binary tree).
def height_of_tree(node): #given input is node
    if node is None:
        return 0
    else:
        return 1 + max(height_of_tree(node.left) + height_of_tree(node.right)) # 1 is added for the root node, and the function will accept the maximum height of either the left or right subtree as the height.

#A function to calculate the height of the tree.
def size_of_tree(node): #given input is node
    if node is None:
        return 0
    else:
        return 1 + size_of_tree(node.left) + size_of_tree(node.right) #to calculate the total size of the tree, just simply add both left and right parts, along with the root(1).

#Converting the created binary tree back to a tuple.
def to_tuple(self):
    if self is None:
        return None
    elif self.left is None and self.right is None:
        return self.key
    else:
        return to_tuple(self.left), self.key, to_tuple(self.right)


#Question to check if the binary tree is the binary search tree, to find the minimum key value, and to find the maximum key value.
def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node): #function to check oif the binary tree is the BST.
    if node is None: #if the node is equal to None, then
        return True, None, None #return true for is a binary search tree, and None for maximum and minimum keys in the tree.

        #assigning variables
        is_bst_l, min_l, max_l = is_bst(node.left)
        is_bst_r, min_r, max_r = is_bst(node.right)

        #to check whether it is a binary search tree,
        is_bst_node = (is_bst_l and is_bst_r and (max_l is None or node.key>max_l) and (min_r is None or node.key < min_r))
        #is_bst_l and is_bst_r signifies that the left and right subtrees are also a binary search tree,
        #max_l is None(that there is no left subtree) or node.key>max_l signifies that if the maximum key of left subtree  is None or its maximum key is less than the present node
        #min_r is None or node.key>min_r signifies that if the minimum key of right subtree  is None or its minimum key is greater than the present node.

        #To find the minimum and maximum keys of tyhe tree,
        min_key = min(remove_none([min_l, node.jey, min_r]))
        max_key = max(remove_none([max_l, node.key, max_r]))

        return is_bst_node, min_key, max_key


#A class BSTNode to represent the nodes of a tree.
class BSTNode():
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

#Note that Python functions are dynamic, i.e., we need not to mention the type of input we are pfoviding to the function.


#A function to insert a value or a node to the BInary Search Tree
def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node #setting now the left inserted node as the node, or the root node so that more insertions can be performed.
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node 
    
#A function to find a node in the bianry search tree.
def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key) # calling the function find recursively on the left node.
    if key > node.key:
        return find(node.right, key)

#A function to update the value of a found node.
def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

#A function to retrieve the nodes, or keys in sorted order
def list_all(node):
    if node is None:
        return []
    else:
        return list_all(node.left) + [node.key, node.value] + list_all(node.right)
        #node.left returns the list of all the nodes at the left, and is recursively calling the function list_all. And similarly for root.right.
        #[node.key, node.value] returns the values at the roots
        #Remember that, inorder traversal of BST always returns keys in the sorted order.
        
#A function to check whether the binary tree is balanced or not.
#For a tree to be balanced, it should follow the following properties;
#1) Ensure that the right and left subtrees are balanced.
#2) Ensure that the difference between heights of left and right subtree is not more than 1.

def is_balanced(node):
    if node is None: #base or end condition in recursion
        return True, 0 #0 is the height of the tree
    balanced_l, height_l = is_balanced(node.left)##checking if the left and right subtrees are balanced by recursively calling a function.
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
    #balanced_l and balanced_r means that both left and right trees are balanced.
    height = 1 + max(height_l, height_r)
    return balanced, height

#A function to create a balanced BST from a sorted list/array of key-value pairs.
#We can use a recursive strategy, turning the midddle element into the root, and recursively creating left and right subtrees.
def make_balanced_bst(data, low=0, high=None, parent=None):
    if high is None:
        high = len(data)-1 #high is set to last index of the data
    if low>high: #when we are left with no more nodes to be balanced.
        return None

    mid = (low+high)//2
    key, value = data[mid]
    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, low, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, high, root)

    return root

#A function for balancing an unbalanced binary tree to a balanced tree.
def balance_bst(node):
    return make_balanced_bst(list_all(node)) #list_all(node) is a function of listing all the nodes in sorted order(inorder traversal) and then balancing it using the make_balanced_bst function.

#For creating tree values,
tree1 = None
for user in users: #users is a defined list of all the users
    tree1 = insert(tree1, user.username, user)

tree2 = balance_bst(tree1)#to balance the tree1.


#This is an iterable class due to the generator functions prsent.
class TreeMap():
    def __init__(self):
        self.root = None #initially root of the TreeMap is set to None

        #these are the special functions
        def __setitem___(self, key, value): #A function combining insert and update
            node = find(self.root, key)#first the node is found with a certain key
            if not node: #if node is not found, i.e., the initial stage where self.root = None, then
                self.root = insert(self.root, key, value) #call the insert function to insert the node with a key and a value with complexity O(log(N))
                self.root = balance_bst(self.root) #after inserting, balancing the tree with complexity O(N)
            else:
                update(self.root, key, value)

        def __getitem__(self, key): #this function lists the nodes
            node = find(self.root, key)
            if node: #if node is found then return its value
                return node.value
            else: #if not found
                return None

        def __iter__(self): #this function is a replacement to the list_all function(returns a generator)
            return (x for x in list_all(self.root))

        def __len__(self):
            return tree_size(self.root) #returns the size of the tree calculating from the root node

        def display(self):
            return display_keys(self.root)

treemap = TreeMap()
print(treemap.root) #at the first, will print None
treemap.display

#to insert,
treemap['radhika'] = radhika
treemap['anjani'] = anjani
treemap['ranjana'] = ranjana

#to find the length of the treemap
len(treemap)

#to retrieve an element,
treemap['radhika']

#to print all the keys and values,
for key, value in treemap:
    print(key, value)
