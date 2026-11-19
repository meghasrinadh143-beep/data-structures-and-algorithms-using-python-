#User String 
'''from collections import UserString
s=UserString(input("Enter string:"))
x=input("Enter prefix:")
y=input("Enter suffix:")
print("Starts with:",s.startswith(x))
print("Ends with :",s.endswith(y))
'''

#check if the given strin is a plandrome or not 
'''from collections import UserString
s=UserString(input("Enter string :"))
if s==s[::-1]:
    print("it is a plandrom ")
else:
    print("it is not a plandrom")'''

#deque from queue
#import deque 
#1. insert - append() - default right side 
#2. insert - appendleft() - only added to right side 
#3. delete - pop() - default deletion on the right side 
#4. delete - popleft() - only deletion on left side 
#5. add element - extend() - default right side 
#6. add element - extendleft() - only on left side 
#7. remove - specific element delete - delete 
#8. reverse - reverse the deque 
#9. rotate() - 1 2 3 4 5, 2(2 times rotation clock wise ) :4 5 1 2 3 /  froanti clock wise rotation we use -2 
#              1 2 3 4 5,-2(2 times rotation of anti clock wise ): 3 4 5 1 2 / fro clock wise -2 
#10. count() - count the occur 
#11. index() - element position 
#12. insert(0,0) 
#13. clear()
#14. copy() - duplicate data creation 
#15. maxlen()


#deque Operation 
#append of deque 
'''from collections import deque
d=deque(map(int,input("Enter elements:").split()))
val=int(input("Enter value to ppend on the right side: "))
d.append(val)
print("deque",d)
val=int(input("Enter the value to append on the left side:"))
d.appendleft(val)
print("deque",d)'''

#pop for deque 
'''from collections import deque
d=deque(map(int,input("Enter the elements:").split()))
x=d.pop()
print("deleted element:",x)
print("deque:",d)
y=d.popleft()
print("deleted element:",y)
print("deque:",d)'''

#add element for deque 
'''from collections import deque
d=deque(map(int,input("Enter elements:").split()))
val=list(map(int,input("Enter the value to extend on right ").split()))
d.extend(val)
print("deque:",d)
val=list(map(int,input("Enter the elements to add on the left :").split()))
d.extendleft(val)
print("Deque:",d)'''

#remove specific elemnts in the deque
'''from collections import deque
d=deque(map(int,input("Enter elements:").split()))
val=int(input("Enter the value to remove :"))
print("deque:",d)
if val in d:
    d.remove(val)
    print("deque:",d)
else:
    print("value not found")'''

#reverse of the deque 
'''from collections import deque
d=deque(map(int,input("Enter the elements :").split()))
d.reverse()
print("reversed deque:",d)'''

#rotate of the deque 
'''from collections import deque
d=deque(map(int,input("Enter the elements:").split()))
r=int(input("Enter value to rotate clock wise:"))
print("deque",d)
d.rotate(r)
print("deque:",d)
r=int(input("Enter value to rotate anti clock wise"))
d.rotate(-r)
print("deque",d)'''

#index operation in deque 
from collections import deque
d=deque(map(int,input("Enter elements:").split()))
print("deque:",d)
x=int(input("Enter value to search the index:"))
print("index:",d.index(x))
# insert operation in deque 
pos=int(input("Enter the position "))
y=int(input("Enter value"))
d.insert(pos,y)
print("deque",d)
#copy operation in deque 
a=d.copy()
print("Duplicate deque :",a)
#clear operation deque
d.clear()
print("deque :",d)