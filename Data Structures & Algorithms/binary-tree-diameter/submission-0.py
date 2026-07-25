# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def calculate_height_and_update_diameter(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        h_left = self.calculate_height_and_update_diameter(root.left)
        h_right = self.calculate_height_and_update_diameter(root.right)
        
        self.diameter = max(self.diameter, h_left + h_right)
        
        return max(h_left, h_right) + 1
        

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.calculate_height_and_update_diameter(root)
        
        return self.diameter
        