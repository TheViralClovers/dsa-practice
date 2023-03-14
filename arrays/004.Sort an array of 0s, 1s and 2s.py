#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        sorted_arr = []
        ele_count = [0,0,0]
        for i in arr:
            if(i==0):
                ele_count[0]+=1
            elif(i==1):
                ele_count[1]+=1
            else:
                ele_count[2]+=1

        for i in range(len(arr)):
            if(ele_count[0]):
                arr[i]=0
                ele_count[0]-=1
            elif(ele_count[1]):
                arr[i]=1
                ele_count[1]-=1
            elif(ele_count[2]):
                arr[i]=2
                ele_count[2]-=1

#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends