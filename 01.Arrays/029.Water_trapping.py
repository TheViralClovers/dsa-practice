#horizontal traversal
class Solution:
    # def trappingWater(self, arr,n):
    #     #Code here
    #     max_height = max(arr)
    #     water_trapped = 0
    #     left = 0
    #     right=n-1
        
    #     for i in range(1,max_height+1):
    #         while arr[left] < i: #left moves to the postion where it is max for the current value of i
    #             left+=1
                
    #         while arr[right] < i: #right moves to the postion where it is max for the current postion of i
    #             right -=1
                
    #         water_trapped+=(right-left+1)
            
    #     water_trapped-=sum(arr)
    #     return water_trapped
    def trappingWater(self,arr, n):
      
    # Indices to traverse the array
        left = 0
        right = n-1
      
        # To store Left max and right max 
        # for two pointers left and right
        l_max = 0
        r_max = 0
      
        # To store the total amount 
        # of rain water trapped
        result = 0
        while (left <= right):
              
            # We need check for minimum of left 
            # and right max for each element
            if r_max <= l_max:
                  
                # Add the difference between 
                #current value and right max at index r
                result += max(0, r_max-arr[right])
                  
                # Update right max
                r_max = max(r_max, arr[right])
                  
                # Update right pointer
                right -= 1
            else:
                  
                # Add the difference between 
                # current value and left max at index l
                result += max(0, l_max-arr[left])
                  
                # Update left max
                l_max = max(l_max, arr[left])
                  
                # Update left pointer
                left += 1
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends