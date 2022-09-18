# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        currmax = [0]
        def helper(root):
            if root == None:
                return 0
            else:
                left = helper(root.left)
                right = helper(root.right)
                if left + right > currmax[0]:
                    currmax[0] = left + right
                return max(left, right) + 1
        helper(root)
        return currmax[0]
                
                
                