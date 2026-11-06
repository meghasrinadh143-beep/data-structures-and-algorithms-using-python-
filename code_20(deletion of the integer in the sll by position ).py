#deletion a value in sll by position 
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("Enter the number od nodes:"))
for i in range(n):
    data=int(input("Enter the data:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("the linkied list is :")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")
pos=int(input("Enter the position to deletion :"))
if pos<1 or head is None:
    print("Invalid position ")
elif pos==1:
    head=head.next
else:
    temp=head
    count=1
    while temp.next and count<pos-1:
        temp=temp.next
        count+=1
    if temp.next is None:
        print("Invalid position")
    else:
        temp.next=temp.next.next
print("After the deletion ")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")'''



#*SINGLY LINKED LIST - DELETION OF A NODE*
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("Enter the number od nodes:"))
for i in range(n):
    data=int(input("Enter the data:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("the linkied list is :")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")
#Ente the value to be deleted in the single linkied list 
value=int(input("Enter the value to delete :"))
if head is None:
    print("SLL is Empty")
elif head.data==value:
    head=head.next
else:
    temp=head
    while temp.next and temp.next.data!=value:
        temp=temp.next
    if temp.next is None:
        print("Value not forund in the SLL")
    else:
        temp.next=temp.next.next
print("After the deletion ")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")'''

#swapping the nodes in the single linkied list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("Enter the number of nodes:"))
for i in range(n):
    data=int(input("Enter the data:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("the linkied list is:")  
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")
prev=None
current=head
while current:
    nextnode=current.next
    current.next=prev
    prev=current 
    current=nextnode
head=prev
print("reversed SLL:")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")