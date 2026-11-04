#single linkied list insert from begining (sll insert from begining)
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter the number of nodes:"))
for i in range(n):
    data=int(input("enter the data:"))
    newnode=node(data)
    newnode.next=head
    head=newnode
print("the linkied list is:")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")'''

#sll insert from end
class node:
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
