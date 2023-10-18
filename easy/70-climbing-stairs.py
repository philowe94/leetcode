import pdb

class Solution:
	def climbStairs(self, n: int) -> int:
		one, two = 2,1

		if n <= 3:
			return n

		for i in range(n-2):
			temp = one
			one = one + two
			two = temp
			
		return one
		
# 5 step staircase
# from step 4, there is one way
# from step 3, there is two ways
# from step 2, there is three ways
# from step 1, there is five ways
# from step 0, there is eight ways