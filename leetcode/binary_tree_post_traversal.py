# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root != None:
            tree_top = []
            tree_node = root
            pre_order = []
            while tree_node!=None or len(tree_top) > 0:
                if tree_node != None:
                    tree_top.append(tree_node)
                    tree_node = tree_node.left
                else:
                    tree_last = tree_top[-1]
                    if tree_last.right != None:
                        tree_node = tree_last.right
                    else:
                        pop_node = tree_top.pop()
                        pre_order.append(pop_node.val)
                        tree_node = tree_top[-1]
            return pre_order
        else:
            return []

def main():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.right = b
    b.left = c
    s = Solution()
    print s.postorderTraversal(a)

if __name__ == '__main__':
    main()


