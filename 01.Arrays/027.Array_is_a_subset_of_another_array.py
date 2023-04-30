#User function Template for python3

def isSubset( a1, a2, n, m):
    isSubset = "Yes"
    a1_freq = dict()
    a2_freq = dict()
            
    for num in a1:
        if num in a1_freq:
            a1_freq[num]+=1
        else:
            a1_freq[num]=1
            
    for num in a2:
        if num in a2_freq:
            a2_freq[num]+=1
        else:
            a2_freq[num]=1  
    # print(a1_freq,a2_freq)
    for num in a2_freq:
        if num in a1_freq:
            if a1_freq[num] < a2_freq[num]:
                isSubset = "No"
        else:
            isSubset = "No"
    
    return isSubset

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends