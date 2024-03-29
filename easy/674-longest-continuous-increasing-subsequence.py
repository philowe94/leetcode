from typing import List
import pdb

class Solution:
	def findLengthOfLCIS(self, nums: List[int]) -> int:
		longestlen = 0
		len = 0
		lastnum = None

		for x in nums:
			if lastnum == None:
				len = 1
				lastnum = x
			elif x > lastnum:
				len += 1
				lastnum = x
			else:
				len = 1
				lastnum = x

			longestlen = max(len, longestlen)
		

		return longestlen

sol = Solution()
print(sol.findLengthOfLCIS([3,0,6,2,4,7,0,0]))