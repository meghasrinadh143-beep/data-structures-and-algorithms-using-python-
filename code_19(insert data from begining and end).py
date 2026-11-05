#insert at end delete at begining 
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None  
head=None
n=int(input("enter the number of nodes:"))
for i in range(n):
    data=int(input("enter the data:"))
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
#delete from begining
if head is None:
    print("sll is empty")
else:
    head=head.next
print("the single linkied list after dilition fro the begining is:")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")'''


#insertion at begining and deletion at end
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=node
head=None
n=int(input("Eter the number of nodes:"))
for i in range(n):
    data=int(input("Enter the data:"))
    newnode=node(data)
    newnode.next=head
    head=newnode
print("the linkied list is:")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
#deletion form end
if head is None:
    print("sll is empty")
elif head.next is None:
    head=None
else:
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None
print("the single linkied list after deletion from the end is:")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")'''


# insertion at position (begining)
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("Enter the number of nodes:"))
for i in range(n):
    data=int(input("Enter the data:"))
    newnode=node(data)
    newnode.next=head
    head=newnode
print("the linkied list is:")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")
#inserting the node at the bigining of the linkied list position
pos=int(input("enter the position to insert the Node:"))
data=int(input("Enter the data to insert:"))
newnode=node(data)
if pos==1:
    newnode.next=head
    head=newnode
else:
    temp=head
    count=1
    while temp and count<pos-1:
        temp=temp.next
        count+=1
    if temp is None:
        print("Invalid position")
    else:
        newnode.next=temp.next
        temp.next=newnode
print("the single linkied list after the insertin is:")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")
