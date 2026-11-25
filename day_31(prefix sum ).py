#find the Prefix Sum of an array
'''arr=list(map(int,input("Enter values : ").split()))
prefix=[]
total=0
for i in range(len(arr)):
    total+=arr[i]
    prefix.append(total)
print('prefix sum :',prefix)'''

#prefix an array with in a range
'''arr=list(map(int,input("Enter the values ").split()))
prefix=[]
total=0
for i in range(len(arr)):
    total+=arr[i]
    prefix.append(total)
print('prefix sum : ',prefix)
s=int(input("Enter starting point : "))
e=int(input("Enter ending point : "))
if s<0 or e>len(arr) or s>e:
    print("Invalid position ")
elif s==0:
    print("Range sum ", prefix[e])
else:
    print("Range sum ",prefix[e]-prefix[s-1])'''


#count the subarrays for the target values 
'''arr=list(map(int,input('Enter the values : ').split()))
target = int(input("Enter target : "))
count=0
for i in range(len(arr)):
    total=0
    for j in range(i,len(arr)):
        total +=arr[j]
        if total==target:
            count+=1
print('coutn : ',count)'''


#prefix - count the number of sub array with only 1 for loop 
arr=list(map(int,input('Enter values : ').split()))
target=int(input("Enter the target value : "))
count=0
total=0
freq={0:1}
for i in range(len(arr)):
    total+=arr[i]
    if total-target in freq:
        count+=freq[total-target]
    freq[total]=freq.get(total,0)+1
print('count : ',count)