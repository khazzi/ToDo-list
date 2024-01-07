#create a list for the data
to_do_list = []

#start creating the functions required in the software

#the add task function
def add_task(task):
    to_do_list.append(task)
    print("Task added succesfully.")

#the view task function
def view_task():
    if not to_do_list:
        print("There's nothing in your To-Do List")

    else:
        print("The contents of your list:")
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}, {task}")

#the remove task function
def remove_task(index):
    if 1 <= index <= len(to_do_list):
        removed_task = to_do_list.pop(index - 1)
        print(f"Task '{removed_task}' has been removed from the list.")
    else: 
        print("Invalid task index.")
#the main program loop
while True:
    print("\n Options")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice from 1 to 4.")

    if choice == "1":
        task = input("Enter the task.")
        add_task(task)
    elif choice == "2":
        view_task()
    elif choice == "3":
        view_task()
        index = int(input("Enter the task index you wish to remove"))
        remove_task(index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice, Please Select a number from 1 to 4.")

#end of program