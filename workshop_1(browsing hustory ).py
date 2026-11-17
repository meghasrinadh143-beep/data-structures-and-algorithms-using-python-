#browsing history 
back=[]
forward=[]
current=""
while True:
    print("\n1.visit")
    print("2.Back")
    print("3.Forward")
    print("4.Display History ")
    print("5.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        website=input("Enter Website:")
        if current !="":
            back.append(current)
        forward.clear()
        current=website 
        #print("visited",current)
    elif ch==2:
        if back:
            forward.append(current)
            current=back.pop()
            #print("current wensite:",current)
        else:
            print("No previous website")
    elif ch==3:
        if forward:
            back.append(current)
            current=forward.pop()
            #print("current website :",current)
        else:
            print("no previous website")
    elif ch==4:
        with open("history.txt",'w') as f :
            for site in back:
                f.write(site+'\n')
            if current :
                f.write (current+'\n')
            for site in forward:
                f.write(site+'\n')
        with open('history.txt','r')as f:
            print(f.read())
    elif ch==5:
        print("Exit")
        break
    else:
        print("Invalid choice , try again")
