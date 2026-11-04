# 1) flip sort or pancake sort 
'''def pancakesort(arr):
    n=len(arr)
    for size in range(n,1,-1):
        max_index=arr.index(max(arr[:size]))
        arr[:max_index+1]=arr[:max_index+1][::-1]
        arr[:size]=arr[:size][::-1]
    return arr
arr=list(map(int,input("Enter the elements :").split()))
print("Sorted array:", pancakesort(arr))'''

# 2) quick sort 
def quicksort(arr):
    n=len(arr)
    if n<1:
        return arr
    pivot=arr[-1]
    left=[x for x in arr[:-1] if x<=pivot]
    right=[x for x in arr[:-1] if x>pivot]
    return quicksort(left)+[pivot]+quicksort(right)
arr=list(map(int,input("Enter the elements:").split()))
print("Sorted array:", quicksort(arr))