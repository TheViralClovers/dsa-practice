#User function Template for python3
#doesnt work
class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
	def find3Numbers(self,A, n, X):
		for num1 in A:
			two_sum_arr = A[:]
			# print(two_sum_arr)
			two_sum_arr.pop(num1)
			# print(two_sum_arr)
			for i in range(len(two_sum_arr)):
					two_sum_arr[i]+=num1
					print(two_sum_arr)
			for num2 in two_sum_arr:
				if X-num2 in A:
					return 1    
			# print(two_sum_arr)
		return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# import atexit
# import io
# import sys

# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER

# @atexit.register

# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    # t = int(input())
    # for i in range(t):
    #     n,X=map(int,input().strip().split())
    #     A=list(map(int,input().strip().split()))
		n = 4
		X =3
		A=[1,2,2,1]
		ob=Solution()
		if(ob.find3Numbers(A,n,X)):
			print(1)
		else:
			print(0)
# } Driver Code Ends