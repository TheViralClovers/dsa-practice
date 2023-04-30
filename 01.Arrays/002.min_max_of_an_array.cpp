//{ Driver Code Starts
/* Driver program to test above function */

#include<iostream>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution
{
   public:
    int findSum(int A[], int N)
    {
    	//code here.
    	int max{-9999999},min{9999999};
    	for(int num=0;num<N;num++){
    	    if(max<A[num]){
    	        max=A[num];
    	    }
    	    if(min>A[num]){
    	        min=A[num];
    	    }
    	}
    	 return max+min;
    }

};

//{ Driver Code Starts.
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int arr[100];

	    for(int i=0;i<n;i++)
	      cin>>arr[i];
	    Solution ob;  
	    int ans=ob.findSum(arr, n);
	    cout<<ans;
	    cout<<"\n";
	}
	return 0;
}

// } Driver Code Ends