#User function Template for python3
"""
    [7, 10, 4, 3, 20, 15]
    if
    swapping7 and 7
    [7, 10, 4, 3, 20, 15]
    if
    swapping10 and 10
    [7, 10, 4, 3, 20, 15]
    if
    swapping4 and 4
    [7, 10, 4, 3, 20, 15]
    if
    swapping3 and 3
    [7, 10, 4, 3, 20, 15]
    [7, 10, 4, 3, 15, 20]
    4
"""
    
def partition(arr,left,right):
        x = arr[right] #storing the value of the right most value to use for swapping
        i=left #storing the value of the left most index for swapping and incrementing, can't increment left directly because, we have used left in for loop
        

        for j in range(left,right):
            # print(arr)
            if arr[j]<=x: #this means that the number from the left side is less than the pivot number x (here arr[right])
                #since this number is less than the number on the right, we swap the numbers with the number on the right
                #i stores the left index
                # print(arr)
                # print("if")
                # print("swapping"+str(arr[i])+" and "+str(arr[j]))
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
            #when the if fails, j will increment as usual, but i wont increment,and i and j will finally be pointing to 2 different numbers to swap
        arr[i],arr[right]=arr[right],arr[i] #this swaps the position  of the number just above pivot with the pivot
        #i stores the count of all the numbers less than pivot element + 1(which gives index of pivot element) (here pivot element is arr[right])
        #i is only meant to increase when it gets a number smaller than pivot
        #j increases no matter what
        # print(arr)
        return i
        
class Solution:
    
        
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        
        # if left == right: #this is when there is only one element
        #     return arr[left]
        
        if(k>0 and k<=r-l+1): # checks if k is smaller than the number of elements in the array
            pivotIndex = partition(arr,l,r)
            
            if(pivotIndex-l==k-1): #k is equal to pivot index
                return arr[pivotIndex]
                
            if(pivotIndex-l>k-1): #k is greater, so recurse in the left subarray
                return self.kthSmallest(arr,l,pivotIndex-1,k)
            
            #else k is smaller so recurse in the right subarray
            return self.kthSmallest(arr,pivotIndex+1,r,k - pivotIndex + l - 1)# why is k-pivotIndex+l-1
        
        # for i in range(k):
        #     min = arr[0]
        #     for j in range(len(arr)):
        #         if(min>arr[j]):
        #             min = arr[j]
        #     # print("{i} min removed")
        #     arr.remove(min)
        # return min

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends