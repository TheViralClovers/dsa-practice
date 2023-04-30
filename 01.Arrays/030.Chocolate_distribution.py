#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        
        if(M==0 or N==0):
            return 0
            
        if(N<M):
            return -1
            
        A.sort()
        
        min_diff = A[N-1]-A[0]
        
        for i in range(len(A)-M+1): #we iterate only till m-1 because, we seek m elements in the array and dont want to go out of bounds
            min_diff = min(min_diff, A[i+M-1]-A[i]) #after sorting the array, we iterate over it , keeping 2 pointers that are m distance apart and calc difference so that number of students gets divided (m-1 because [i to i+m-1] has m elements as i is also included in range like 0 to m-1 has m elements)
            
        return min_diff

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends