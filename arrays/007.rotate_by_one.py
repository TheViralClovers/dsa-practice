#User function Template for python3

def rotate( arr, n):
    last = arr[n-1]
    # for i in range(arr):
        # arr[i+1]=arr[i]
    i=1
    while(i!=n):
        arr[n-i]=arr[n-i-1]
        i+=1
    arr[0]=last



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends