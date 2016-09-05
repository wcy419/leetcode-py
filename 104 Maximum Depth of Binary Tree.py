class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        else:    
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.left.left = TreeNode(8)
    print Solution().maxDepth(root)
