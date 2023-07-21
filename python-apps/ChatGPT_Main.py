import os

todos = []

# Check if the file exists before reading it
if os.path.exists('python-apps/todos.txt'):
    with open('python-apps/todos.txt', 'r') as file:
        todos = file.readlines()

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a new task: ") + "\n"
            todos.append(todo)

            with open('python-apps/todos.txt', 'w') as file:
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

                with open('python-apps/todos.txt', 'w') as file:
                    file.writelines(todos)
            except (ValueError, IndexError):
                print("Invalid task number. Please try again.")

        case 'complete':
            try:
                number = int(input("Enter the number of the task to complete: "))
                number -= 1
                todos.pop(number)

                with open('python-apps/todos.txt', 'w') as file:
                    file.writelines(todos)
            except (ValueError, IndexError):
                print("Invalid task number. Please try again.")

        case 'exit':
            break

        case _:
            print("You entered an unknown command.")

print("Bye!")
