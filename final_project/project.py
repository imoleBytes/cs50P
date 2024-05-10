""" TodoList Project:
    A command line implementation of todo list using python and its library.
"""
from rich.console import Console
from rich.table import Table
from models import Todo
import os, sys, json


console = Console()

todos = []
try:

    with open("data.json") as f:
        temp = json.load(f)
    if temp:
        for i in temp:
            todos.append(Todo(i['title'], i['done']))
except Exception as e:
    pass


def main():
    """Entry point of program"""
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
                        persist_data()
                        display_dashboard()
                case '2':
                    print('editing...')
                    if not todos:
                        console.print('[blink i red]************** No todos here! ****************---[/blink i red]')
                    try:
                        edit(todos)
                        persist_data()
                    except IndexError as e:
                        print(e)

                    display_dashboard()
                case '3':
                    print('removing...')
                    if todos:
                        try:
                            num_to_remove = int(input('remove #: '))
                            if num_to_remove < 1 or num_to_remove > len(todos):
                                raise IndexError('Out of range, Please enter the correct number to remove')
                            else:
                                remove(todos, num_to_remove)
                                persist_data()
                        except IndexError as e:
                            print(e)
                        except:
                            print('Invalid Number')
                        display_dashboard()
                    else:
                        console.print('[blink i red]************** No todos here! ****************---[/blink i red]')

                case '4':
                    if todos:
                        complete(todos)
                        persist_data()
                        display_dashboard()
                    else:
                        console.print("[bold red]There's Nothing here to toggle![/bold red]")
                
                case '5':
                    os.system('clear')
                    show_table()
                    console.print('[bold cyan]Thanks for using the program...[/bold cyan]')
                    sys.exit()


def add(title):
    """Function add:
        Args:
            title <list_of_todo_obj>
        return:
            void    
    """
    item = Todo(title)
    todos.append((item))

def persist_data():
    """ Persists data to data.json"""
    with open("data.json", "w") as f:
        objs = [i.to_dict() for i in todos]
        json.dump(objs, f)



def edit(todos: list):
    """edits todo item"""
    ed = int(input("Enter Item umber(#): ").strip())
    if ed not in range(1, len(todos) + 1):
        raise IndexError(f'Item out of range (Range is 1 - {len(todos)})')
    newtitle = input('Edit your to do: ').strip()
    
    todos[ed - 1].title = newtitle

def complete(todos: list):
    """Toggles Done attribute of the todo item"""

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
    """removes an item from the list"""

    todos.pop(num-1)


def display_dashboard():
    """display the dashboard"""

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
    return None


def show_table():
    """contructs the table consisting the items"""

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
            
        console.print(table)

    else:
        console.print('[blink i red]************** No todos here! ****************---[/blink i red]')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print()
        console.print('[bold cyan]Thanks for using the program...[/bold cyan]')
        sys.exit(1)
