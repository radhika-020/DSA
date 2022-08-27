#Given a  binary tree root, and we need to check whether it is symmetric around its center(is it a mirror itself).
#Symmetric means, that the reverse of left and right subtree are equal and the root must have the same values for both the trees..

#To find the tree sum, 

def tree_sum(root):
    if root is None:
        return 0
    else:
        left = tree_sum(root.left)
        right = tree_sum(root.right)
        return root.val + left + right

#For two subtrees to be symmetric with two root values, or we can say two trees are symmetric with two given root values,
def are_symmetric(root1, root2):
    if root1 is None and root2 is None: #if both of hem doesn,t exists, i.e., the root values doesn't exists for both the trees, then in that case they are symmetric.
        return True
    elif ((root1 is None) != root2 is None) or root1.val != root2.val:
        return False
    else:
        return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left) 

#For a single tree,
def is_symmetric(root):
    if root is None:
        return True
    else:
        return are_symmetric(root.left, root.right)

#Time Complexity :- O(N)
#Space Complexity :- O(NlogN)
