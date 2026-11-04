#traversals of array
#pattern of  an array
'''n=int(input("enter the size of matrix:"))
arr=[[0]*n for _ in range(n)]
print(arr)
top=0
bottom=n-1
left=0
right=n-1
num=1
while top<=bottom and left<=right:
    #top, from left to right
    for i in range(left, right+1):
        arr[top][i]= num
        num+=1
    top+=1
    #right, from top to bottom
    for i in range(top, bottom+1):
        arr[i][right]= num
        num+=1
    right-=1
    #bottom, from right  to left
    for i in range(right,left-1,-1):
        arr[bottom][i]=num
        num+=1
    bottom-=1
    #left, from bottom to top
    for i in range(bottom,top-1,-1):
        arr[i][left]=num
        num+=1
    left+=1
for row in arr:
    for x in row:
        print(f"{x:4}",end=' ')
    print()'''

n=int(input("Enter the size of the matrix :"))
arr=[]
for i in range(n):
    arr.append(list(map(int,input("enter numbers: ").split())))
top=0
bottom=n-1
left=0
right=n-1
num=1
while top<=bottom and left<=right:
    #top , from left to right
    for i in range(left , right+1):
        print(arr[top][i],end=" ")
    top+=1
    #right , from top to bottom
    for i in range(top , bottom+1):
        print(arr[i][right],end=" ")
    right-=1
    #bottom , from right to left 
    for i in range(right,left-1,-1):
        print(arr[bottom][i],end=" ")
    bottom-=1
    #left , from bottom to top
    for i in range(bottom, top-1,-1):
        print(arr[i][left],end=" ")
    left+=1