# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root != None:
            tree_top = []
            tree_node = root
            pre_order = []
            while tree_node!=None or len(tree_top) > 0:
                if tree_node != None:
                    tree_top.append(tree_node)
                    tree_node = tree_node.left
                else:
                    pop_node = tree_top.pop()
                    pre_order.append(pop_node.val)
                    tree_node = pop_node.right
            return pre_order
        else:
            return []


