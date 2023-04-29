class Solution:

  # Function to find maximum
  # product subarray
	def maxProduct(self,arr, n):
		minVal = arr[0]
		maxVal = arr[0]
	 
		res = arr[0]
	 
		for i in range(1, n, 1):
			 
			# When multiplied by -ve number,
			# maxVal becomes minVal
			# and minVal becomes maxVal.
			if (arr[i] < 0):
				temp = maxVal
				maxVal = minVal
				minVal = temp
				 
			# maxVal and minVal stores the
			# product of subarray ending at arr[i].
			maxVal = max(arr[i], maxVal * arr[i])
			minVal = min(arr[i], minVal * arr[i])
	 
			# Max Product of array.
			res = max(res, maxVal)
	 
		# Return maximum product
		# found in array.
		return res