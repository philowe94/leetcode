from typing import List

class Solution:
	def sortColors(self, nums: List[int]) -> None:
		colorcounts = [0,0,0]

		for num in nums:
			colorcounts[num] += 1

		idx = 0
		for i, colorcount in enumerate(colorcounts):
			for x in range(colorcount):
				nums[idx] = i
				idx += 1
		
		return nums
	
sol = Solution()

nums = [2,0,2,1,1,0]
print(sol.sortColors(nums))
