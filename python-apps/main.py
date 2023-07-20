# user_prompt = "Enter a todo: "

todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter an action: ")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo 
        case 'complete':
            number = int(input("Number of of task to delete: "))
            todos.pop(number -1 )
        case 'exit':
            break
        case _:
            print("You entered an unknown command.")
        
print("Bye!")
     
#      old code:
# case 'show' | 'display':
#             for item in todos:
#                 item = item.title()
#                 print(item)

# while True:
#     todo = input(user_prompt)
#     todos = [todo]
#     print(todos)

# lines 13 to 16
# case 'show' | 'display':
#             for index, item in enumerate(todos):
#                 item = item.title()
#                 print(index, '-', item)