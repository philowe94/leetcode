import pdb

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
		
		if not root:
			return null
		
		if val = root.val:
			return root
		elif val > root.val:
			return searchBST(root.right, val)
		elif val < root.val:
			return searchBST(root.left, val)
		
