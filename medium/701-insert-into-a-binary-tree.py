import pdb

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
		
		if not root:
			return None
		
		elif val > root.val:
			if not root.right:
				root.right = TreeNode(val)
			else:
				self.insertIntoBST(root.right, val)
		elif val < root.val:
			if not root.left:
				root.left = TreeNode(val)
			else:
				self.insertIntoBST(root.left, val)

		return root
		
