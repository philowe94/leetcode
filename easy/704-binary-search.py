import pdb
from typing import List

class Solution:
	def bsearch(self, nums:List[int], left:int, mid: int, right:int, target: int):

		if left > right:
			return -1

		if target == nums[mid]:
			return mid
		elif target > nums[mid]:
			return self.bsearch(nums, mid+1, (mid+1+right)//2, right, target)
		else:
			return self.bsearch(nums, left, (left+mid-1)//2, mid-1, target)

	def search(self, nums: List[int], target: int) -> int:
		left = 0
		right = len(nums) -1
		mid = (left+right)//2

		return self.bsearch(nums, left, mid, right, target)
		
	
sol = Solution()

nums = [-1,0,3,5,9,12]
target = 9
print(sol.search(nums, target))
	

