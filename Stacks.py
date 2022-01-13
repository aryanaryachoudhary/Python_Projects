#A program to perform the following operation in a Stack using List
#          1. Push      2. Pop   3. Display   4. exit
           
def isEmpty(stk):
    if (stk==[]):
        return True
    else:
        return False

def Push(stk,item):
    global top
    stk.append(item)
    if top==None:
        top=0
    else:
        top=top+1

def Pop(stk):
    global top
    if isEmpty(stk):
        return "Underflow"
    else:
        item=stk.pop()
        if(len(stk)==0):
            top=None
        else:
            top=top-1
        return item

def Display(stk):
    global top
    if (isEmpty(stk)):
        print("Underflow stack is empty can not display")
    else:
        for i in range(top,-1,-1):
            print (stk[i])

#_main_
Stack=[]
top=None
ans='y'
while(ans=='y'):
    print("Stack Operations")
    print("Press 1 to Push: ")
    print("Press 2 to Pop: ")
    print("Press 3 to Display: ")
    print("Press 4 to exit: ")
    ch=int(input("Enter your choice: "))
    if (ch==1):
        item=int(input("Enter Item Value: "))
        Push(Stack,item)
    elif(ch==2):
        item=Pop(Stack)
        if (item=="Underflow"):
            print("Underflow ! Stack is Empty")
        else:
            print("Popped item is ",item)
    elif(ch==3):
        Display(Stack)
    elif(ch==4):
        break
    else:
        print("Invalid choice")
        
    ans=input("Do you wish to continue (y/n): ")
    if(ans=="n"):
        print("Thank You for using this Program!")

#End of Program!
