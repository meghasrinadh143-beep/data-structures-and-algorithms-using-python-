#time complexity and space complexity 

#O(1)- constant time complexity space complexity = O(1)
'''n=int(input("Enter a number: "))
print(n+100)'''

#O(n) - linear time complexity, linear space complexity = O(n)
'''n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(i,end=" ")'''

#O(n) - linear time complexity, constant space complexity = O(1)
'''n=int(input("Enter a number :" ))
arr=[]
for i in range(n):
    num=int(input("Enter a number:"))
    arr.append(num)
print("the numbers are :",arr)'''

# 4) O(n^2) - quadratic time complexity, constant space complexity = O(1)
'''n=int(input("Enter a number: "))
num=1
for i in range(n):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()'''

# 5) logarithmic time complexity O(log n) 
'''n=int(input("enter n:"))
while n>1:
    print(n)
    n//=2
print(1)'''

# 6) O(n (log n)) - logarithmic time complexity
'''n=int(input("enter n:"))
for i in range(n):
    j=n
    while j>1:
        j//=2
        print(j,end=" ")
print("done")'''

# 7) O(2^n) - exponential time complexity
def count(n):
    if n==0:
        return 1
    return count(n-1) + count(n-1)
n=int(input("Enter a number:"))
print("reslt :",count(n))
