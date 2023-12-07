# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
		stack = []
		curr = root

		# this uses inorder traversal
		# instead of recursion, we use a stack and a while loop
		# the stack lets us travel back up the nodes
		# and find the kth lowest by decrementing k at each node we hit inorder

		while stack or curr:
			while curr: # get lowest while keeping track of path in stack
				stack.append(curr)
				curr = curr.left

			curr = stack.pop() # curr is null atm, so pop the lowest off the stack
			# if curr was null, this moves back up the stack

			k -= 1 # k is 1-indexed, so decrement before checking

			if k == 0:
				return curr.val
			
			curr = curr.right # go right
			# if there is no right but still a stack,
			# we stay in the loop

			