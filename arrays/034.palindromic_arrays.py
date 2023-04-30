# Your task is to complete this function
# Function should return True/False or 1/0
def isPalindrome(num):
    temp = num
    rev_num = 0
    while(num>0):
        digit=num%10
        num//=10
        rev_num = rev_num*10+digit
        
    return temp==rev_num

def PalinArray(arr ,n):
    # Code here
    for num in arr:
        if not isPalindrome(num):
            return 0
    
    return 1



#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends