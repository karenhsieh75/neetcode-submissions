# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        if not root:
            return res

        q = deque()
        q.append(root)

        while q:
            length = len(q)
            for i in range(length):

                node = q.popleft()
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None

                if i == length - 1:
                    res.append(node.val)
        
        return res


        