# user_prompt = "Enter a todo: "
todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter an action: ") + "\n"
            
            # file = open('text-todo.txt', 'r')
            # todos = file.readlines()
            # file.close()

            with open('text-todo.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('text-todo.txt', 'w') as file:
                file.writelines(todos)

            # file = open('text-todo.txt', 'w')
            # file.writelines(todos)
            # file.close()

        case 'show' | 'display':
        #     file = open('text-todo.txt', 'r')
        #     todos = file.readlines()
        #     file.close()

            with open('text-todo.txt', 'r') as file:
                todos = file.readlines()

            new_todos = []

            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)
            # print(todos)
            new_todos = [item.strip('\n') for item in todos]
            
            
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item.strip('')}"
                print(row, end = '')
                # print("length is", index + 1)
                # print((len(todos)))
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            
            with open('text-todo.txt', 'r') as file:
                todos = file.readlines()
            # print('Here is existing tasks: ', todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo  + '\n'

            print('Here is New list of tasks: ', todos)

            with open('text-todo.txt', 'w') as file:
                file.writelines(todos)
            
            
    
        case 'complete':
            number = int(input("Number of of task to delete: "))
            with open('text-todo.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            task_to_remove = todos[index].strip('\n')
            todos.pop(index)
            with open('text-todo.txt', 'w') as file:
                file.writelines(todos)
                
            message = f"Task {task_to_remove} was removed."
            print(message)
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