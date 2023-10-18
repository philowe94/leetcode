#sort an array
#merge sort solution
import pdb
from typing import List


class Solution:

	def merge(self, nums: List[int], startIdx:int, midIdx:int, endIdx:int) -> List[int]:

		# copy the left and right halfs to temp arrays
		leftArr = nums[startIdx:midIdx+1]
		rightArr = nums[midIdx+1:endIdx+1]
		
		# index vars
		i = 0 # index for leftArr
		j = 0 # index for rightArr
		k = startIdx # index for nums

		# merge the two half arrays
		while i < len(leftArr) and j < len(rightArr):
			if leftArr[i] <= rightArr[j]:
				nums[k] = leftArr[i]
				i += 1
			else:
				nums[k] = rightArr[j]
				j += 1
			k += 1

		# handle remaining elements
		while i < len(leftArr):
			nums[k] = leftArr[i]
			i += 1
			k += 1
		while j < len(rightArr):
			nums[k] = rightArr[j]
			j += 1
			k += 1

		return nums

	def mergeSort(self, nums: List[int], startIdx:int, endIdx:int) -> List[int]:
		
		# if indexes specify array of length 1 or less
		# return the array as is
		if (endIdx - startIdx + 1) <= 1:
			return nums

		# if the array is greater than length 1
		# calculate the middle index and split into two subproblems
		midIdx = (startIdx + endIdx) // 2
		self.mergeSort(nums, startIdx, midIdx)
		self.mergeSort(nums, midIdx+1, endIdx)
		
		# merge the subproblems
		self.merge(nums, startIdx, midIdx, endIdx)

	def sortArray(self, nums: List[int]) -> List[int]:
		self.mergeSort(nums, 0, len(nums))

		return nums
	
arr = [5,2,3,1, 623, 123, 3456, 123, 456, 665, 83, 5, 345, 12325123]
soln = Solution()
print(soln.sortArray(arr))