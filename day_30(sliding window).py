# Sliding window of kth largest slide
'''arr=list(map(int,input("Enter value : ").split()))
k=int(input("Enter slide size: "))
if k<=0 or k>len(arr):
    print("Invalid window size : ")
else:
    w_sum=0
    for i in range(k):
        w_sum+=arr[i]
    max_sum=w_sum
    for i in range(k,len(arr)):
        w_sum=w_sum-arr[i-k]+arr[i]
        if w_sum > max_sum:
            max_sum = w_sum
    print("output :",max_sum)
'''
# sliding window - average of all subarrays
'''arr=list(map(int,input("Enter the value : ").split()))
k=int(input("Enter slide size : "))
if k<=0 or k>len(arr):
    print("Invalid window size")
else:
    w_sum=0
    for i in range(k):
        w_sum+=arr[i]
    print(w_sum/k,end=' ')
    for i in range(k,len(arr)):
        w_sum = w_sum-arr[i-k]+arr[i]
        print(w_sum/k,end=' ')'''

# sliding number - print the first negitive number in the slide   12 -1 -7 8 -15 30 16 28 
'''arr = list(map(int,input("Enter element : ").split()))
k = int(input("Enter window size : "))
if k<= 0 or k> len(arr):
    print("Invalid window size ")
else:
    queue=[]
    result = []
    for i in range(len(arr)):
        if arr[i] < 0:
            queue.append(i)
        if i>=k-1:
            while queue and queue[0]<= i-k:
                queue.pop(0)
            if queue:
                result.append(arr[queue[0]])
            else:
                result.append(0)
    print(result)'''

#                   or 

arr=list(map(int,input("Enter elements : ").split()))
k=int(input("Enter window size : "))
if k<=0 or k>len(arr):
    print("Invalid window size ")
else:
    for i in range(len(arr)-k+1):
        found=False
        for j in range(i,i+k):
            if arr[j]<0:
                print(arr[j],end=' ')
                found=True
                break
        if found==False:
            print(0,end=' ')
