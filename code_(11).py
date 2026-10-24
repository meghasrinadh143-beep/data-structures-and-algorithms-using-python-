# 1) bubble sort example
'''arr=list(map(int,input("Enter the elements for the array :").split()))
n=len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(*arr)'''

# 2) selection sort 
""" arr=list(map(int,input("Enter the elements for the array : ").split()))
n=len(arr)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(*arr) """

# 3) insertion sort 
arr=list(map(int,input("Enter the elements for the array :").split()))
n=len(arr)
for i in range(1,n):
    m=arr[i]
    j=i-1
    while j>=0 and arr[j]>m:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=m
print(*arr)