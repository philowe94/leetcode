import pdb

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guess(num: int) -> int:
	pick = 6
	if num > pick:
		return -1
	elif num < pick:
		return 1
	else:
		return 0

class Solution:

	def guessNumber(self, n: int) -> int:
		left = 1
		right = n

		while left <= right:
			mid = (left + right) // 2
			if guess(mid) == 1: # if guess is lower than the num
				left = mid+1
			elif guess(mid) == -1: # if guess is higher than the num
				right = mid-1
			else:
				break

		return (left+right)//2

sol = Solution()

print(sol.guessNumber(10))