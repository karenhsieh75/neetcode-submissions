# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        n = 0
        stack = []
        cur = root

        while cur or stack:
            # go to the left most node
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # now cur = None, we can start popping from the stack
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            
            # finish processing the node itself, move on to right
            cur = cur.right

