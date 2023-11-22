import pdb
from typing import List
import random

class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		
		pivotidx = random.randint(0, len(nums)-1)
		pivot = nums[pivotidx]

		A1 = [] # big elements
		A2 = [] # small elements

		for i in range(0, len(nums)):
			if nums[i] > pivot:
				A1.append(nums[i])
			elif nums[i] < pivot:
				A2.append(nums[i])

		#recursive call
		if k <= len(A1): 
			return self.findKthLargest(A1, k)
		elif k > len(nums) - len(A2):
			return self.findKthLargest(A2, k-(len(nums) - len(A2)))
		else: 
			return pivot

arr = [3,1,2,4]
soln = Solution()
print(soln.findKthLargest(arr, 3))


