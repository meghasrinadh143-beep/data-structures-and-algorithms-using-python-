#double or doubly linked list insert at beginning
'''class node:
    def __init__(self, data):
        self.data = data
        self.prev =None
        self.next = None
head = None
n= int(input("Enter number of nodes:"))
for i in range(n):
    data = int(input("Enter value:"))
    newnode = node(data)
    newnode.next = head
    if head is not None:
        head.prev = newnode
    head = newnode
print("Double linked list:")
temp = head
while temp:
    print(temp.data, end= '<->')
    temp = temp.next
print("Tail")'''


#Doubly Linked List - Insertion at End and deleting at the end 
'''class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("enter value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("Double linked list:")
temp=head

while temp:
    print(temp.data,end='<->')
    temp=temp.next
print("tail")
#delete at the end 
if head is None:
    print("Double linked list empty")
elif head.next is None:
    head=None
else:
    temp=head
    while temp.next:
        temp=temp.next
    temp.prev.next=None
print("After deleting at end Double linked list")
temp=head
while temp:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")'''

#Doubly Linked List - Insertion at End and Deletion at Beginning
'''class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("enter value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("Double linked list:")
temp=head

while temp:
    print(temp.data,end='<->')
    temp=temp.next
print("tail")
#delete at the begining
if head is None:
    print("Dll is empty")
else:
    head=head.next
    if head is not None:
        head.prev =None
print("After deleting at end Dll")
temp=head 
while temp:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")'''

# question need to complete 
#insert at position ,delete at position and delete the value in single linkied list 


#Doubly Linked List - Insertion at Specific Position
'''class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("enter value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("Double linked list:")
temp=head

while temp:
    print(temp.data,end='<->')
    temp=temp.next
print("tail")
#insertion at position 
pos=int(input("Enter position:"))
val=int(input("Enter value:"))
newnode=node(val)
if pos<1:
    print("invalid Position ....")
elif pos==1:
    newnode.next=head
    if head:
        head.prev=newnode
    head=newnode
else:
    temp=head
    count=1
    while temp and count<pos-1:
        temp=temp.next
        count+=1
    if temp is None:
        print("Invalid position....")
    else:
        newnode.next=temp.next
        newnode.prev=temp
        if temp.next:
            temp.next.prev=newnode
        temp.next=newnode
print("Ater inserting at position DLL")
temp=head
while temp:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")'''
