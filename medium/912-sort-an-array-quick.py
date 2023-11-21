#sort an array
#quick sort solution
import pdb
from typing import List


class Solution:

	def mean3(self, arr, a, b, c):
		if arr[a] <= arr[b] <= arr[c] or arr[c] <= arr[b] <= arr[a]:
			return arr[b], b
		elif arr[b] <= arr[a] <= arr[c] or arr[c] <= arr[a] <= arr[b]:
			return arr[a], a
		else:
			return arr[c], c

	def quickSort(self, arr: List[int], startIdx:int, endIdx:int) -> List[int]:
		
		# if indexes specify array of length 1 or less
		# return the array as is
		if (endIdx - startIdx + 1) <= 1:
			return arr

		# if the array is greater than length 1
		# set pivot value to the middle value between the start, end, and middle of arr
		(pivot, pivotIdx) = self.mean3(arr, startIdx, endIdx, (startIdx+endIdx)//2)

		# if pivot is not the endIdx value, swap it to end
		if arr[endIdx] != pivot:
			arr[pivotIdx] = arr[endIdx]
			arr[endIdx] = pivot

		# set the left pointer to the starting index of the array
		left = startIdx

		# traverse the array (or the subarray specified by startIdx and endIdx)
		# if an element is found smaller than the pivot;
		# swap that element with the element in the left pointer
		# then increment the left pointer
		for i in range(startIdx, endIdx+1):
			if(arr[i] < pivot):
				temp = arr[i]
				arr[i] = arr[left]
				arr[left] = temp
				left += 1

		# perform pivot swap
		arr[endIdx] = arr[left]
		arr[left] = pivot

		# recursive calls
		self.quickSort(arr, startIdx, left-1)
		self.quickSort(arr, left+1, endIdx)
		


	def sortArray(self, nums: List[int]) -> List[int]:
		self.quickSort(nums, 0, len(nums)-1)

		return nums
	
arr = [-1,2,-8,-10]
soln = Solution()
print(soln.sortArray(arr))


