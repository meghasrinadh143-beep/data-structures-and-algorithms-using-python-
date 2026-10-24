#searching in array in 1D/2D
# 1) seraching an element and returning it's index value in 1D array 
'''arr=list(map(int,input("Enter values of arr").split())) #n repesent row of the code 
search=int(input("Enter the elements to be searched :"))
found=False
for i in range(len(arr)):
    if arr[i]==search:
        print("elements found at : ",i)
        found=True
        break
if not found:
    print("element is not in range")'''

# 2) searching an element and returnaing it's index value in 2D array 
"""n=int(input("Enter the size:"))  #n repesent row of the code 
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
search=int(input("Enter elements to be searched : "))
found=False
for i in range(n):
    for j in range(n):
        if arr[i][j]==search:
            print("Element found at:",i,j)
            found=True
            break
if not found:
    print("Element is out of range")"""

# 3) sum of the matrix in 2D array 
'''n=int(input("Enter the size :")) #n repesent row of the code 
s=0
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        s+=arr[i][j]
print("Sum is :",s)'''

# 4) sumation of rows and colums in the program 
'''n=int(input("Enter the size of the matrix :"))
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    row_sum=0
    for j in range(n):
        row_sum+=arr[i][j]
    print("Row:",i+1,"Sum:",row_sum)
for j in range(n):
    col_sum=0
    for i in range(n):
        col_sum+=arr[i][j]
    print("column :",j+1,"Sum : ",col_sum)'''

# 5) sumation of diagonal in the matrix
'''n=int(input("Enter the size of the matrix :"))
arr=[]
di=0
ad=0
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if i==j:
            di+=arr[i][j]
        if i+j==n-1:
            ad+=arr[i][j]
print("Diagnol sum:",di)
print("Anti-Diagnol:",ad)'''

# 6) 