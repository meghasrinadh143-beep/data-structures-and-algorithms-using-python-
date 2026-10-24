# binary search 
# 1)Write a program to implement Binary Search to search an element in a sorted array. Take array elements and key element from user.
'''arr=list(map(int,input("Enter the array elements:").split()))
arr.sort()   # To sort the array for the program 
n=int(input("Enter to be searched value :"))
l=0
r=len(arr)-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]==n:
        print("element found at index :",mid)
        break
    elif arr[mid]<n:
        l=mid+1
    else:
        r=mid-1
else:
    print("element not found")'''

# 2) by using binary search find the square root 
'''n=int(input("Enter the value :"))
l=0
h=n
while l<=h:
    mid=(l+h)//2
    if mid*mid==n:
        print("square root is ",mid)
        break
    elif mid*mid<n:

        l=mid+1
    else:
        h=mid-1
else:
    print("inter square root :",h)'''

