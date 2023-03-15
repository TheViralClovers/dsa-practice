def move_negatives(arr):
    low = 0
    high = len(arr)-1
    while(low<high):
        if(arr[low]>0):
            arr[low],arr[high] = arr[high],arr[low]
            high-=1
        if(arr[low]<=0):
            low+=1
    print(arr)


move_negatives([1,-1,2,-2,-3,-6,-8,34,56])