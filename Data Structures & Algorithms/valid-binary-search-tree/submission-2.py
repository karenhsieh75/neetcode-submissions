# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(root: Optional[TreeNode]) -> Tuple[int, int]:

            if not root:
                return -1001, 1001
            
            max_left, min_left = dfs(root.left)
            max_right, min_right = dfs(root.right)

            if max_left >= root.val or min_right <= root.val:
                self.res = False
            
            max_val = max(max_left, max_right, root.val)
            min_val = min(min_left, min_right, root.val)

            return max_val, min_val

        dfs(root)
        return self.res
