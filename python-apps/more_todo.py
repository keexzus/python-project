
# user_prompt = "Enter a todo: "

todos = []

while True:
    user_action = input("Type add, show, or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter an action: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
        
print("Bye!")
     

# while True:
#     todo = input(user_prompt)
#     todos = [todo]
#     print(todos)