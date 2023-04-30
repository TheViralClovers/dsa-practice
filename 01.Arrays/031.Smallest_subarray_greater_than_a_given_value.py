class Solution:
    def smallestSubWithSum(self, a, n, x):
        # Your code goes here 
        start = 0
        end = 0
        curr_sum=0
        min_length = n+1
        
        # for i in range(n):
        #     if total_sum < x:
        #         total_sum+=a[right]
        #         count+=1
        #         right+=1
        #     elif total_sum-a[left]>x:
        #         total_sum-=a[left]
        #         count-=1
        #         left+=1
                
        # return count
        
        while end < n:
            #keep adding till sum>=x
            while (curr_sum <=x and end<n):
                curr_sum += a[end]
                end += 1
                
            #start subtracting till sum is just above x
            while(curr_sum > x and start<n):
                min_length = min((end-start),min_length)
                curr_sum-=a[start]
                start+=1
                
        return min_length



#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends