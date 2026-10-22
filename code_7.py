# 1) traverse an array and 100 to each element
'''arr=list(map(int,input("Enter elements : ") .split()))
for val in arr:
    print(val+100,end=" ")'''

# 2) summate the values in an array 
'''arr=list(map(int,input("Enter elemenst : ").split()))
total=0
for val in arr:
    total+=val
print("Sum : ",total)'''

# 3) find the largest value in array 
'''arr=list(map(int,input("Enter elements : ").split()))
max=arr[0]
for val in arr:
    if val>max:
        max=val
print("largest number is:",max)'''

# 4) find the lowest number in the array 
'''arr=list(map(int,input("Enter elements:").split()))
min=arr[0]
for val in arr:
    if val<min:
        min=val
print("smallest numbse is :",min)'''

# 5) reverse an array 
'''arr=list(map(int,input("Enter elements:").split()))
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=" ")'''

# 6) remove the duplicate in an array 
'''arr=list(map(int,input("Enter elements : ").split()))
result=[]
for i in arr:
    if i not in result:
        result.append(i)
print(*result)'''

# 7) print the count of even and odd number in array 
'''arr=list(map(int,input("Enter elements:").split()))
even=0
odd=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even count :",even)
print("odd count : ", odd)'''

# 8) rotate an array in clock wise direction
'''arr=list(map(int,input("Enter elements :" ).split()))
k=int(input("Enter no.of rotation for the array :"))
k%=len(arr)
arr=arr[k:]+arr[:k]
print(arr)'''

# 9) rotate an array in anti-clock wise direction
'''arr=list(map(int,input("Enter elements:").split()))
k=int(input("Enter rotation u want:"))
k%=len(arr)
arr=arr[-k:]+arr[:-k]
print(*arr)'''
