#collection of queue 
#Counter 
'''from collections import Counter
num=input("Enter value ").split()
c=Counter(num)
print("Counter:",c)'''

#defaultdict
'''from collections import defaultdict
d=defaultdict(int)
n=int(input("Enter number of elements :"))
for i in range(n):
    val=input("Enter value:")
    d[val]+=1
print("Dictonary:",dict(d))
'''

#OrdereDict
'''from collections import OrderedDict
d=OrderedDict()
n=int(input("Enter number of elements:"))
for i in range(n):
    key=input("Enter key :")
    val=input("Enter value :")
    d[key]=val
print("Orderd Dictonary :",d)
'''

#namedtuple
'''from collections import namedtuple
student=namedtuple("Student",["name","age","marks"])
name=input("Enter name :")
age=int(input("Enter age:"))
marks=int(input("Enter latest marks :"))
s=student(name,age,marks)
print("Student ",s)
print("Marks:",s.marks)
print("Age",s.age)
'''

#ChainMap
'''from collections import ChainMap
d1={}
d2={} 
n=int(input("Enter number of elements in d1:"))
for i in range(n):
    key=input("Enter  key:")
    val=input("Enter value:")
    d1[key]=val
n=int(input("Enter number of elements in d2:"))
for i in range(n):
    key=input("Enter key:")
    val=input("Enter value:")
    d2[key]=val
c=ChainMap(d1,d2)
print("1st dictonary :",d1)
print("2nd dictonary :",d2)
print("Chain Map:",c)'''

#UserDict,UserList
from collections import UserDict,UserList
class MyDict(UserDict):
    def add_data(self,key,value):
        self.data[key]=value 
d=MyDict()
n=int(input("Enter number of elements :"))
for i in range(n):
    key=input("Enter key: ")
    value=input("Enter value:")
    d.add_data(key,value)
print("Disctionary ",d)

class MyList(UserList):
    def add_element(self,value):
        self.data.append(value)
l=MyList()
num=input("Enter number").split()
for i in num:
    l.add_element(i)
print("List:",l)
