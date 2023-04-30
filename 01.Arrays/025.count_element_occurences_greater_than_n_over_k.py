#User function Template for python3


class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        #Your code here
        num_count = dict()
        
        for num in arr:
            if num in num_count:
                num_count[num]+=1
            else:
                num_count[num]=1
                
        n_over_k = n/k
        count = 0
        
        for num in num_count:
            if num_count[num] > n_over_k:
                count+=1
                
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends