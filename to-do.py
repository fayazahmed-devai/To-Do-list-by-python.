tasks=[]
def add_task():
    task=input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully")
def view_task():
    if len(tasks)==0:
        print("no tasks available")
    else:
        print("\nYour  to-do list:")
        for i, task in enumerate(tasks, start=1):
            print(i, ".", task)
def delete_task():
    view_task()

    if len(tasks) >0:
        number = int(input("enter task number to delete:"))

        if 1<= number <= len(tasks):
            removed=tasks.pop(number-1)
            print(removed, "deleted successfully")
        else:
            print("invalid task number")

while True:
    print("\n===== to-do list =====")
    print("1. add tasks")
    print("2. view tasks")
    print("3. delete tasks")
    print("4. exit")
    choice = input("enter your choice:")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("thank you for choosing the to-do list created by fayaz with love")
        break
    else:
        print("Invalid choice, choice between 1-4 only......try again")