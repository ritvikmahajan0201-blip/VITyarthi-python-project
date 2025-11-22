#Python Project
#To do list creator and manipulator 
def priority_lev(priority_level,task,status): #function 1
    if priority_level == 1:
        dic_tasks[task] = ['High',status]
        return
    elif priority_level == 2:
        dic_tasks[task] = ['Medium',status]
        return
    else:
        dic_tasks[task] = ['Low',status]
        return
    
def viewalltasks(): # function 2 
    for task_number, (key, value) in enumerate(dic_tasks.items(), start=1):
        print(f"""Task Number: {task_number}
Task: {key}
Priority Level : {value[0]}
Status: {value[1]}""")
        

dic_tasks = {}
no_oftasks = int(input("Please enter the number of tasks you have: "))
for i in range(1,no_oftasks+1):
    task = input(f"Please enter task {i}: ").lower()
    priority_level = int(input("""Please enter the level of priority this task requires: 
Enter 1 for 'High'
Enter 2 for 'Medium'
Enter 3 for 'Low': """))
    status = int(input("""Please enter the status of the task
Enter 1 if pending
Enter 2 if Done: """))
    if status == 1:
        priority_lev(priority_level,task,'pending')
    else:
        priority_lev(priority_level,task,'done')

print("All tasks successfully added into the list.")
print(dic_tasks)
#options
while True:
    print("""Please choose from the options below:
1) View all tasks
2) Add a new task
3) Delete an old task
4) change the priority level of a particular task
5) change status of a particular task
6) View tasks of a particular Priority""")
    choice = int(input("Please enter your choice(1-6): "))
    if choice == 1:
        viewalltasks()
        choice = input("Do you want to continue(Y/N): ")
        if choice.lower() == 'y':
            continue
        else:
            break
    elif choice == 2:
        new_task = input("Please enter the new task: ")
        priority_level = int(input("""Please enter the level of priority this task requires: 
    Enter 1 for 'High'
    Enter 2 for 'Medium'
    Enter 3 for 'Low': """))
        status = int(input("""Please enter the status of the task
    Enter 1 if pending
    Enter 2 if Done: """))
        if status == 1:
            priority_lev(priority_level,new_task,'pending')
        else:
            priority_lev(priority_level,new_task,'done')
        print("New task successfully added")
        viewalltasks()
        choice = input("Do you want to continue(Y/N): ")
        if choice.lower() == 'y':
            continue
        else:
            break
    elif choice == 3:
        viewalltasks()
        delete_task = input("Please enter the name of the task you want to delete: ").lower()
        del dic_tasks[delete_task]
        print("The task is successfully removed from the list")
        viewalltasks()
        choice = input("Do you want to continue(Y/N): ")
        if choice.lower() == 'y':
            continue
        else:
            break
    elif choice == 4:
        viewalltasks()
        while True:
            try:
                task = input('Please enter the name of the task that you want to change the priority for: ')
                new_priority = int(input("""Please enter the new priority: 
            Enter 1 for 'High'
            Enter 2 for 'Medium'
            Enter 3 for 'Low': """))
                priority_lev(new_priority,task,status = dic_tasks[task][1])
                print("Priority successfully updated")
                viewalltasks()
            except KeyError:
                print("Please enter a valid task name")
                continue
            else:
                break
        choice = input("Do you want to continue(Y/N): ")
        if choice.lower() == 'y':
            continue
        else:
            break
    elif choice == 5:
        viewalltasks()
        task_name = input("Please enter the name of the task for which you want to change the status for: ")
        New_status = int(input("""Please enter the new status of the task
Enter 1 if pending
Enter 2 if Done: """))
        if New_status == 1:
            dic_tasks[task_name][1] = 'pending'
        elif New_status == 2:
            dic_tasks[task_name][1] = 'done'
        print("Status successfully updated")
        viewalltasks()
        choice = input("Do you want to continue(Y/N): ")
        if choice.lower() == 'y':
            continue
        else:
            break
    elif choice ==6 :
        priority_level = int(input("""Please enter the priority level of which you want to view the tasks for
Enter 1 for 'High'
Enter 2 for 'Medium'
Enter 3 for 'Low': """))
        if priority_level == 1:
            for key,value in dic_tasks.items():
                if value[0] == 'High': 
                    print(f"""Task: {key}
Priority Level : {value[0]}
status: {value[1]}""")
        elif priority_level == 2:
            for key,value in dic_tasks.items():
                if value[0] == 'Medium':
                    print(f"""Task: {key}
Priority Level : {value[0]}
status: {value[1]}""")
        elif priority_level == 3:
            for key,value in dic_tasks.items():
                if value[0] == 'Low':
                    print(f"""Task: {key}
Priority Level : {value[0]}
status: {value[1]}""")
        choice = input("Do you want to continue(Y/N): ")
        if choice.lower() == 'y':
            continue
        else:
            break



print("Quitted from program")
print("Thankyou for using the program")
    
