from collections import deque #double ended queue which I think means you can pop from both ends

#strategy: go through the tree level by level, starting at the root.
# print the value of the root
# add the children of the root to the queue
# pop the root from the queue
# print the value of the next node in the queue
# add the children of the next node to the queue
# pop the next node from the queue
# repeat until the queue is empty

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def bfs(root): # breadth first search, given a starting node
	queue = deque() # create a deque

	if root: # if the root exists, add it to the deque
		queue.append(root)
	
	level = 0 # initialize the level to 0
	while len(queue) > 0: # while the queue is not empty
		print("level", level)

		for i in range(len(queue)):
			node = queue.popleft()
			print(node.value)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		level += 1

# initialize a tree for testing
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

bfs(root) # call the function with the root of the tree