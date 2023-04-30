#User function Template for python3

class Solution:
	def find_median(self, v):
		# Code here
		v.sort()
# 		print(len(v)+1)
# 		return v[len(v)//2]
		if len(v)%2:
			return v[len(v)//2]
			
		return (v[len(v)//2]+v[(len(v)-1)//2])//2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends