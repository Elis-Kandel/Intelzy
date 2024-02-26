
while True:
    name=input("Name")
    age=input("Age")
    content=[]
    
    with open("text.txt","r") as file:
        content=file.readlines()
    
    content.append(f'''
Name:{name}
Age:{age}''')
    
    
    with open('text.txt','w') as file:
        for line in content:
            file.write(line)
            
            
    user_input= input("Do you want to continue")
    if user_input=="yes":
        continue
    else:
        break
        
        