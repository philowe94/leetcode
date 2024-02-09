import pdb


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key == root.val:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Find the min from the right subtree
            # sets successor to the smallest node larger
            # than the node we are deleting
            successor = root.right
            while successor.left:
                successor = successor.left

            # replace the matching node with the value
            # of the successor node
            root.val = successor.val

            # delete the
            root.right = self.deleteNode(root.right, successor.val)

        return root
