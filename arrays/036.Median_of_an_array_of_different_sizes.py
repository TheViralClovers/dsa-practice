#User function Template for python3

class Solution:
	
			#code here

	# Method to find median
	def Median(self, A, B):

		# Assumption both A and B cannot be empty
		n = len(A)
		m = len(B)
		if (n > m):
			return self.Median(B, A) # Swapping to make A smaller

		start = 0
		end = n
		realmidinmergedarray = (n + m + 1) // 2

		while (start <= end):
			mid = (start + end) // 2
			leftAsize = mid
			leftBsize = realmidinmergedarray - mid

			# checking overflow of indices
			leftA = A[leftAsize - 1] if (leftAsize > 0) else float('-inf')
			leftB = B[leftBsize - 1] if (leftBsize > 0) else float('-inf')
			rightA = A[leftAsize] if (leftAsize < n) else float('inf')
			rightB = B[leftBsize] if (leftBsize < m) else float('inf')

			# if correct partition is done
			if leftA <= rightB and leftB <= rightA:
				if ((m + n) % 2 == 0):
					return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
				return max(leftA, leftB)

			elif (leftA > rightB):
				end = mid - 1
			else:
				start = mid + 1

	def MedianOfArrays(self, array1, array2):
		res = self.Median(array1,array2)
		if int(res) == res:
			return int(res)
		return res

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	tcs=int(input())

	for _ in range(tcs):
		m = input()
		arr1=[int(x) for x in input().split()]
		n = input()
		arr2=[int(x) for x in input().split()]
		
		
		ob = Solution()
		print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends