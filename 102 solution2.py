class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        stack,queue,res,nCount=[root],[],[[root.val]],1
        while stack:
            temp=stack.pop(0)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
            nCount-=1
            
            res+=[[x.val for x in stack]]
            nCount=len(stack)
        return res

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().levelOrder(root)
    print result
