#User function Template for python3
import math
class Solution:
    def getPairsCount(self, arr, n, k):
        freq= {}
        count = 0
        
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        for i in arr:
            if k - i in freq:
                count+=freq[k-i]
                
        for i in range(n): #this removes any element that has been repeated twice
            if(k-arr[i]==arr[i]):
                count-=1

        return int(count/2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends