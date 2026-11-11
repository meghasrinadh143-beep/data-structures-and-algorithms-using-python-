#Circular linked list - create
'''class node:
    def __init__(self, data):
        self.data= data
        self.next= None
head= None
n= int(input("Enter no.of nodes: "))
for i in range(n):
    data= int(input("Enter value: "))
    newnode=node(data)
    if head is None:
        head= newnode
        temp= head
    else:
        temp.next= newnode
        temp= newnode
if head is not None:
    temp.next= head
if head is None:
    print("SLL is empty ")
else:
    temp= head
    while True:
        print(temp.data, end= "->")
        temp=temp.next
        if temp== head:
            break
    print("Back to head ")'''
    

#circular linked list

'''class node:
    def __init__(self, data):
        self.data= data
        self.next= None
head= None
n= int(input("Enter no.of nodes: "))
for i in range(n):
    data= int(input("Enter value: "))
    newnode=node(data)
    if head is None:
        head= newnode
        temp= head
    else:
        temp.next= newnode
        temp= newnode
if head is not None:
    temp.next= head
if head is None:
    print("SLL is empty ")
else:
    temp= head
    while True:
        print(temp.data, end= "->")
        temp=temp.next
        if temp== head:
            break
c    print("Back to head ")
start= int(input("Enter starting point: "))
temp= head
while temp and temp.data != start:
    temp= temp.next
    if temp==head:
        break
if temp is None or temp.data != start:
    print("Starting value is not found!!!!")
else:
    print("Circular traversal: ")
    start_node= temp
    while True:
        print(temp.data, end="->")
        temp=temp.next
        if temp== start_node:
            break
    print("Back to head ")'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head

# Step 1: Find the middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

# Step 2: Reverse the second half
    prev = None
    temp = slow

    while temp:
    next_node = temp.next
    temp.next = prev
    prev = temp
    temp = next_node

# Step 3: Compare both halves
    left = head
    right = prev

    while right:
    if left.val != right.val:
        return False

    left = left.next
    right = right.next

        return True