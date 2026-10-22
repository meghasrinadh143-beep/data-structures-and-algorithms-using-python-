# 1) strong number - math approach
'''n=int(input("Enter a number:"))
copy=n
total=0
while n!=0:
    d=n%10
    f=1#(or) math.factorial(f)
    i=1
    while i<=d:
        f*=1
        i+=1
    total+=f
    n//=10
if total == copy:
    print(copy," The given number is a strong number")
else :
    print(copy,"The given number is not a strong number")'''

# 2) fabnoic series 
# 1/2!+2/3!+3/4!+........n
'''n=int(input("Enter a number:"))
s=0
f=1
for i in range(1, n+1):
    f*=i+1
    s+=i/f
print("The Output is:",s)'''

# 3) naive approach - find the occurance of the numbers 
'''arr=list(map(int ,input("Enter elements:").split()))
value=int(input("Enter a value:"))
count=0
for i in arr:
    if i==value:
        count+=1
print(value,"Occurances are:", count)'''

# 4) brute force approach - finding all possiility
'''arr=list(map(int,input("Enter Elements:").split()))
target=int(input("Enter value:"))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print(arr[i],arr[j])'''