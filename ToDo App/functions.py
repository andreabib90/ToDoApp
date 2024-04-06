FILEPATH = "todos.txt"

# Get the list of todos from the text file
def get_todos(filepath=FILEPATH):
    """ Read the todos text file."""
    with open(filepath, 'r') as file:
            todos = file.readlines()
    return todos
# Update the list of todos text file
def write_todos(todos, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
            file.writelines(todos)


if __name__ == "__main__":
    print("Hello")