# 1) greedy approach 
'''coins=list(map(int, input("Enter coins:").split()))
amount=(int(input("Enter amount:")))
total_count=0
for coin in coins:
    count=amount//coin
    if count>0:
        print(coin,"rupees:",count)
        total_count+=count
        amount%=coin
print("Total coins:",total_count)'''

# 2) backtracking (head recursion)
'''n=int(input("Enter n:"))
def backtrack(s):
    if len(s)==n:
        print(s)
        return
    backtrack(s+"0")
    backtrack(s+"1")
backtrack("")'''

# 3) tail recursion (backtracking)
'''def num(n):
    if n==0:
        return
    num(n-1)
    print(n,end=" ") 
n=int(input("Enter N:"))
num(n)'''

# 4) nested recursion (backtracking)
'''def func(n):
    if n>10:
        return
    return(func(func(n+2)))
n=int(input("Enter n :"))
print(func(n))'''
