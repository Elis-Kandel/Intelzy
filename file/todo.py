def read_todo():
    with open("todo1.txt","r") as file:
        tasks=file.read().splitlines()
        return tasks
def write_todo(tasks):
    with open("todo1.txt","w") as file:
        for task in tasks:
            file.write(f"{task}\n")
        
def todo_list():
    tasks=read_todo()
    while True:
        if len(tasks)>0:
            for i, task in enumerate(tasks):
                print(f'{i+1}. {task}')
        user_input=input("Enter 'add', 'mark', 'remove' or 'quit'").lower()
        if  user_input== "quit":
            write_todo(tasks)
            print("Good Bye")
            break
        elif user_input=="add":
            task=input("Enter a task")
            tasks.append(task)
        elif user_input=="mark":
            task_id=int(input("Enter task id to mark as completed"))-1
            if task_id<len(tasks) and task_id>=0:
                tasks[task_id]=(f'{tasks[task_id]}-Completed')
            else:
                print("Id Invalid")
        elif user_input=="remove":
            task_id=int(input("Enter task id to remove"))-1
            if task_id<len(tasks) and task_id>=0:
                del tasks[task_id]
            else:
                print("Id Invalid")
        else:
            continue
    
todo_list()