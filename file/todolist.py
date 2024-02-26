content=[]
def add_items():
    global content
    work_left=input("Make a remainder")
    with open("todo.txt","r") as file:
        content=file.readlines()
    content.append(work_left+"\n")
    print(content)
    with open("todo.txt","w") as file:
        for line in content:
            file.write(line)
    
def remove_items():
    global content
    rem=input("What do you want to remove")
    remove=(rem+'\n')
    with open("todo.txt","r") as file:
        content=file.readlines()

    try:
        content.remove(remove)
    except Exception:
        print("This doesnt exist")
    print(content)
    with open("todo.txt","w") as file:
        for line in content:
            file.write(line)
    
while True:
    user_wants=input("A for Add, R for Remove, C to stop adding")
    if(user_wants.upper()=='A'):
        add_items()
        
    elif(user_wants.upper()=="R"):
        remove_items()
    else:
        break
