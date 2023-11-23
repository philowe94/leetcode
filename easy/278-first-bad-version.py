def isBadVersion():
	True

class Solution:
	def firstBadVersion(self, n: int) -> int:
		# this is just binary search??

		left, right = 1, n

		while left <= right:
			mid = (left+right)//2
			if mid == 1:
				if isBadVersion(mid):
					return mid
				else:
					return 2
			
			current = isBadVersion(mid)
			previous = isBadVersion(mid-1)
			if not previous and current: #if prev is not bad and curr is bad
				return mid
			elif current: #if mid is bad and prev is also bad
				right = mid-1
			elif not current: #if mid is good
				left = mid+1
			else:
				break

		return (left+right)//2
