#sort an array
#insertion sort solution
#this solution does not pass the leetcode because insertion is too slow
#however neetcode puts this problem under the insertion sort lesson so
#take it up with them
import pdb
from typing import List


class Solution:
	def sortArray(self, nums: List[int]) -> List[int]:
		for i, x in enumerate(nums):
			j = i-1
			while j >= 0 and nums[j] > nums [j+1]:
				temp = nums[j]
				nums[j] = nums[j+1]
				nums[j+1] = temp
				j -= 1
				breakpoint()

		return nums
	
arr = [5,2,3,1]
soln = Solution()
print(soln.sortArray(arr))