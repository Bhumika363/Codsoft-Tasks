todo_list=[]     
def add_task():
    task=input("Enter a task: ")
    todo_list.append({"Task":task,"Status":"pending"})
    print("New Task Added Successfully!\n")
def view_task():
    print("Your Todo List: ")
    if len(todo_list)==0:
        print("No pending tasks!")
    else:
        for index,task in enumerate(todo_list,1):
            print(f"{index}:{task['Task']}-{task['Status']}")
    print("\n")
def remove_task():
    if len(todo_list)==0:   
        print("List is Empty!")
    else:
        search_index=int(input("Enter the task that you want to remove: ")) - 1
        if 0 <= search_index<len(todo_list):
            removed_task=todo_list.pop(search_index)
            print(f"Task Removed:{removed_task}")
        else:
            print("Invalid Task Number.")
def mark_task():
    if len(todo_list)==0:   
        print("List is Empty!")
    else:
        search_index=int(input("Enter the task that you want to mark as done: ")) - 1
        if 0 <= search_index<len(todo_list):   
            todo_list[search_index]['Status']="done"
            print(f"Task:{todo_list[search_index]['Task']} has been marked done.")
        else:
            print("Invalid Task Number:")
def list():
    while(True):
        print("*** THE LIST FOLLOWS ***")
        print("1. Add a new task")
        print("2. View the tasks")
        print("3. Remove a task")
        print("4. Mark a task as done")
        print("5. Exit")
        your_choice=input("Enter your choice:")
        if your_choice=="1":
            add_task()
        elif your_choice=="2":
            view_task()
        elif your_choice=="3":
            remove_task()
        elif your_choice=="4":
            mark_task()
        elif your_choice=="5":
            print("EXITING THE APPLICATION.")
            exit()   
        else:
            print("Invalid choice.\n Try Again!") 
list()




    