tasks = []

def show_tasks():
    print("\nTask List:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task[1] else "✗"
        print(f"{i}. {task[0]} [{status}]")

while True:
    print("\n1- Add Task\n2- Show Tasks\n3- Complete Task\n4- Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task_name = input("Enter task name: ")
        tasks.append([task_name, False])
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        task_number = int(input("Completed task number: "))
        if 0 < task_number <= len(tasks):
            tasks[task_number-1][1] = True
    elif choice == "4":
        break
    else:
        print("Invalid option")
