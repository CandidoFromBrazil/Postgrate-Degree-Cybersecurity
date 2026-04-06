def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    todo_list = []
    
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            print("\nYOUR TASKS:")
            if not todo_list:
                print("Your list is empty.")
            else:
                for index, task in enumerate(todo_list, start=1):
                    print(f"{index}. {task}")

        elif choice == '2':
            new_task = input("Enter the task: ")
            todo_list.append(new_task)
            print("Task added!")

        elif choice == '3':
            if not todo_list:
                print("Nothing to remove.")
                continue
            
            # Show list so user knows what index to pick
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
                
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()