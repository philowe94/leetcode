import pdb
from typing import List

class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		
		leftptr = 0

		#put big nums on left half and small nums on right half
		for i, x in enumerate(nums):
			if x > nums[leftptr]:
				nums[i] = nums[leftptr]
				nums[leftptr] = x
				leftptr += 1
		
		if leftptr == 0:
			leftptr += 1

		leftarr = nums[:leftptr]
		rightarr = nums[leftptr:]

		if len(nums) <= 2 and k <=2:
			return nums[k-1]

		#we need the arr with the same or larger size to k
		if leftptr >= k:
			return self.findKthLargest(leftarr, k)
		else:
			return self.findKthLargest(rightarr, k-len(leftarr))
		

arr = [3,1,2,4]
soln = Solution()
print(soln.findKthLargest(arr, 2))


