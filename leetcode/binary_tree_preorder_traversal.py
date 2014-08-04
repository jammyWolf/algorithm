
#Defition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        tree_top = []
        pre_order = []
        if root != None:
            tree_top.append(root)
            while len(tree_top) > 0:
                data_pre = tree_top.pop()
                pre_order.append(data_pre.val)
                if data_pre.right != None:
                    tree_top.append(data_pre.right)
                if data_pre.left != None:
                    tree_top.append(data_pre.left)
            return pre_order
        else:
            return []



