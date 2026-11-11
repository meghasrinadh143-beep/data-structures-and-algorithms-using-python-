#Push operation 
'''stack=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    val=int(input("Enter a value:"))
    stack.append(val)
print("Stack:",stack)
print("Peek:",stack[-1])
#Delete operation in Stack Data Structure
if len(stack)==0:
    print("Stack Empty!!!!")
else:
    print("Deleted elements:",stack.pop())
print("Stack:",stack)
print("Peek:",stack[-1])'''


#push operation delete all value till Stack empty 
'''stack=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    val = int(input("Enter the value:"))
    stack.append(val)
    print("Stack:",stack)
while len(stack)>0:
    print(stack.pop(),"deleted")
print("Empty Stack",stack)'''

#push operation till overflow 
'''stack=[]
size=int(input("Enter Size:"))
n=int(input("Enter number of elements:"))
for i in range(n):
    val=int(input("Enter the value:"))
    if len(stack)==size:
        print("stack Overflow..........")
    else:
        stack.append(val)
        print(val,"inserted")
print("Stack:",stack)'''

#push operation and merge 2 stack 
'''stack1=[]
stack2=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    val=int(input("Enter the value:"))
    stack1.append(val)
print("stack1;",stack1)
for i in range(n):
    val=int(input("Enter the values:"))
    stack2.append(val)
print("Stack2",stack2)
stack1.extend(stack2)
stack1.sort()
print(stack1)'''



stack1=[]
stack2=[]
stack3=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    val=int(input("Enter the value:"))
    stack1.append(val)
print("stack1;",stack1)
for i in range(n):
    val=int(input("Enter the values:"))
    stack2.append(val)
print("Stack2",stack2)

i,j=0,0
while i<len(stack1) and j<len(stack2):
    if stack1[i]<stack2[j]:
        stack3.append(stack1[i])
        i+=1
    else:
        stack3.append(stack2[j])
        j+=1
while i<len(stack1):
    stack3.append(stack1[i])
    i+=1
while j<len(stack2):
    stack3.append(stack2[j])
    j+=1
print("Merged Stack:",stack3)