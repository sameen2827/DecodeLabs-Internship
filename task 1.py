def show_menu():
    print("\n====== TO-DO LIST ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


def main():
    tasks = []  

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        
        if choice == "1":
            task = input("Enter your task: ")
            tasks.append(task)
            print("Task added successfully!")

        
        elif choice == "2":
            if len(tasks) == 0:
                print("No tasks available.")
            else:
                print("\n Your Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

       
        elif choice == "3":
            if len(tasks) == 0:
                print(" No tasks to delete.")
            else:
                print("\n Your Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                try:
                    num = int(input("Enter task number to delete: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f" Removed: {removed}")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a valid number.")

       
        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")



if __name__ == "__main__":
    main()