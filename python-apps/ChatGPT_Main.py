import os

todos = []


def reset_file_to_empty():
    # Check if the file exists before resetting it
    if os.path.exists('python-apps/todosChat.txt'):
        with open('python-apps/todosChat.txt', 'w') as file:
            file.truncate(0)  # Truncate the file to remove all contents
            print('All tasks deleted.')

# Rest of the code remains the same


# Check if the file exists before reading it
if os.path.exists('python-apps/todosChat.txt'):
    with open('python-apps/todosChat.txt', 'r') as file:
        todos = file.readlines()

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a new task: ") + "\n"
            todos.append(todo)

            with open('python-apps/todosChat.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            try:
                number = int(input("Enter the number of the task to edit: "))
                number -= 1
                new_todo = input("Enter the new task: ")
                todos[number] = new_todo + "\n"

                with open('python-apps/todosChat.txt', 'w') as file:
                    file.writelines(todos)
            except (ValueError, IndexError):
                print("Invalid task number. Please try again.")

        case 'complete':
            try:
                number = int(input("Enter the number of the task to complete: "))
                number -= 1
                todos.pop(number)

                with open('python-apps/todosChat.txt', 'w') as file:
                    file.writelines(todos)
            except (ValueError, IndexError):
                print("Invalid task number. Please try again.")

        case 'reset':  
            reset_file_to_empty()
            todos = []  # Also reset the in-memory list
            print("File reset to empty.")

        case 'exit':
            break

        case _:
            print("You entered an unknown command.")

print("Bye!")
