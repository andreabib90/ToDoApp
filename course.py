from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        # Open and close the file to read
        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        # Clean up the list with list comprehension
        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        try:
            index = int(user_action[5:]) - 1
            new_todo = input("New todo: ")

            todos = get_todos()

            todos[index] = new_todo + "\n"

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            index = int(user_action[9:]) - 1

            todos = get_todos()
            
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")

