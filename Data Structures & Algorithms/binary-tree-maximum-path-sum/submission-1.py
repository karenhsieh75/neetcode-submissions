# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(root: Optional[TreeNode]) -> int:
            # important note: the path can only be split once
            # calculate the value when split at the current node to find max
            # return the value when NOT split at the current node (for parent to split)

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            value_if_split = root.val + left + right
            value_if_not_split = root.val + max(left, right, 0)
            self.res = max(self.res, value_if_split, value_if_not_split)
            
            return value_if_not_split
        
        dfs(root)
        return self.res

            

        