""" TodoList Project:
    A commandline implementation of the todo list using python and its library.
"""
from rich.console import Console
from rich.table import Table
from models import Todo
import os, sys, time, json


console = Console()

todos = []
with open("data.json") as f:
    temp = json.load(f)
if temp:
    for i in temp:
        todos.append(Todo(i['title'], i['done']))


def main():
    while True:
        display_dashboard()
        while True:
            user_input = input('Enter Option Number (#): ').strip()
            if user_input not in ['1', '2', '3', '4', '5']:
                break

            match user_input:
                case '1':
                    console.print('[blue]Creating a to do item[/blue]')
                    item = input('Enter todo title: ').strip()
                    if item:
                        add(item)
                        display_dashboard()
                case '2':
                    print('editing...')
                    try:
                        edit(todos)
                    except IndexError as e:
                        print(e)

                    display_dashboard()
                case '3':
                    print('removing...')
                    if todos:
                        while True:
                            try:
                                num_to_remove = int(input('remove #: '))
                                if num_to_remove < 1 or num_to_remove > len(todos):
                                    raise IndexError('Out of range, Please enter the correct number to remove')
                                break
                            except IndexError as e:
                                print(e)
                            except:
                                print('Invalid Number')

                            
                        remove(todos, num_to_remove)
                        
                        display_dashboard()
                    else:
                        print('Table is empty!')
                case '4':
                    print('completing an item')
                    complete(todos)
                    display_dashboard()
                
                case '5':
                    os.system('clear')
                    show_table()
                    print('exiting...')
                    sys.exit()


def add(title):
    global todos
    item = Todo(title)
    todos.append((item))


def edit(todos: list):
    ed = int(input("Enter Item umber(#): ").strip())
    if ed not in range(1, len(todos) + 1):
        raise IndexError(f'Item out of range (Range is 1 - {len(todos)})')
    newtitle = input('Edit your to do: ').strip()
    
    todos[ed - 1].title = newtitle

def complete(todos: list):
    while True:
        num = input("Toggle Done status for item number #?: ")
        if num == 'exit':
            break
        try:
            num = int(num)
        except:
            print('Invalid entry!')
        if num not in range(1, len(todos) + 1):
            print(f'Please enter a valid number (1-{len(todos)})')
        else:
            todos[num - 1].done = not todos[num - 1].done
            break


def remove(todos: list, num):
    todos.pop(num-1)


def display_dashboard():
    os.system('clear')
    print("................................................\n")
    show_table()
    print("\n................................................")
    print("""Options
          1. Add
          2. Edit
          3. Remove
          4. Complete
          5. Exit
          """)


def show_table():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Number (#)")
    table.add_column("Todo item")
    table.add_column("Done")
    
    if todos:
        for i in range(len(todos)):
            if todos[i].done == True:
                title = f"[s]{todos[i].title}[/s]"
                done = f"[s]{todos[i].done}[/s]"
                table.add_row(str(i + 1), title, done)
            else:
                table.add_row(str(i + 1), todos[i].title, str(todos[i].done))
            
            # print(f"{i + 1}  - {str(todos[i])}")
        console.print(table)

    else:
        console.print('[i]************** No todos here! ****************---[/i]')


if __name__ == "__main__":
    main()
