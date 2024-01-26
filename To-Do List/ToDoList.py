tasks = []
quit = True
def show():
    if not tasks: 
        print("No tasks available.")
    else:
        print("Tasks:\n")
        for index, task in enumerate(tasks,start=1):
            print(f"{index}. {task}")
def add():
    i = input("Enter Task: ")
    tasks.append(i)
    print("Task added succesfully.")
    
def update():
    show()

    index = int(input("Enter index: "))
    if 1<= index <= len(tasks):
        update_task = input("Enter updated task: ")
        tasks[index-1] = update_task
        print("Update suceesfully")
    else:
        print("Invalid index. Please enter a valid index.")
    
while quit:
    print("\nOptions:")
    print("1. Show Tasks")
    print("2. Add Tasks")
    print("3. Update Tasks")
    print("4. Quit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue
    
    if choice == 1:
        show()
    elif choice == 2:
        add()
    elif choice == 3:
        update()
    elif choice == 4:
        print("Exiting Program.")
        quit = False
    else:
        print('"Please choose correct option."')
