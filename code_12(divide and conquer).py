# 1) merge sort
def mergsort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=mergsort(arr[:mid])
    right=mergsort(arr[mid:])
    result=[]
    while left and right :
        if left[0]<right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result+left+right
arr=list(map(int,input("enter the elements for the array :").split()))
print(mergsort(arr))