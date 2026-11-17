#implemantation of stack 
#prefix
exp=input("Enter a expression :")   
stack=[]
result=""
def priority(op):
    if op=='^':
        return 3
    elif op in '*/':
        return 2 
    elif op in '+-':
        return 1
    return 0
exp=exp[::-1]
for ch in exp:
    if ch.isalnum():
        result+=ch
    else:
        while stack and priority(stack [-1])>priority(ch):
            result +=stack.pop()
        stack.append(ch)
while stack :
    result+=stack.pop()
print("Prefix:", result[::-1])
