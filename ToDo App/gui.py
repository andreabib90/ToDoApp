import functions
import PySimpleGUI as sg
import time
import os


# Create "todos.txt" file if not present
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")

# Create GUI widgets and window
clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo.", key="todo")
add_button = sg.Button("Add")

list_of_todos = functions.get_todos()
cleaned_todos = [item.strip() for item in list_of_todos]

list_box = sg.Listbox(values=cleaned_todos,
                    key='todos',
                    enable_events=True,
                    size=[45, 10]
                )
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App", 
                   layout=[
                           [clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]], 
                   font=('Helvetica', 16))


while True:
    event, values = window.read(timeout=200)

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    # Match different events from user interaction
    match event:
        case "Add":
            todos = functions.get_todos()
            todo = values['todo'] + "\n"
            todos.append(todo)
            functions.write_todos(todos)
            window['todos'].update(values=[item.strip() for item in todos])

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
            
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit + "\n")
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=[item.strip() for item in todos])
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 16))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete + "\n")
                functions.write_todos(todos)
                clean_todos = [item.strip() for item in todos]
                window['todos'].update(values=clean_todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 16))

        case "todos":
            window["todo"].update(value=values['todos'][0].strip())

        case "Exit":
            break
            
        case sg.WIN_CLOSED:
            break

window.close()

