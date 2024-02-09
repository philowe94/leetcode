# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        returnarr = []

        if root:
            queue.append(root)

        level = 0
        levelarr = []
        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.popleft()
                levelarr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            returnarr.append(levelarr)
            levelarr = []
        
        return returnarr

        