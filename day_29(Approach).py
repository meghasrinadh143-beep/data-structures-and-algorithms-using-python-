#Approach :
# 1. two pointer approach 
# a) 
# b)

#reverse a array 
#1 2 3 4 5 6
#1         r
#6 5 4 3 2 1  l+=1, r-=1
#  1       r
#6 5 3 4 2 1  l+=1, r-=1
#    1     r
#6 5 4 3 2 1  l>r   r<l
#true loop breaks 
#shooping in ekart 
#bio informatics
#2 4 6 8 
#10
#2 8 
#4 6


#double ended - two pointer approach - reverse an array 
'''arr=list(map(int,input("Enter the value").split()))
left = 0
right = len(arr) - 1
while left<right :
    arr[left],arr[right] = arr[right],arr[left]
    left+=1
    right-=1
    print(arr)'''
#  Write a Python program to reverse a given string using the two-pointer method without using slicing [::-1] or any built-in reverse() function.
'''text = input("Enter text:")
arr = list(text)
left = 0
right = len(arr) - 1
while left < right :
    arr[left],arr[right] = arr[right],arr[left]
    left+=1
    right-=1
result = ''
for ch in arr:
    result+=ch
print(result)'''

#double ended - two pointer approach - 2 value sum 
arr = list(map(int,input("enter value:").split()))
target=int(input("Enter the target :"))
left = 0
right = len(arr) - 1
while left < right :
    if target == arr[left]+arr[right]:
        print("pairfound : ",arr[left],arr[right])
        left+=1
    else:
        right -= 1


#One ended - two pointer approach - move 0 to end 
arr = list(map(int,input("Enter the value :").split()))
left = 0
right = 0 
while right < len(arr):
    if arr[right] != 0:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
    right += 1
print(arr)
