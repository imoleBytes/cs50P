""" TodoList Project:
    A commandline implementation of the todo list using python and its library.
"""
from models import Todo
from utils import complete, remove, edit
import os, sys, time


todos = []

def main():
    while True:
        display_dashboard()
        while True:
            user_input = input('Enter Option Number (#): ').strip()
            if user_input not in ['1', '2', '3', '4', '5']:
                break

            match user_input:
                case '1':
                    print('Creating a to do item')
                    item = input('Enter todo title: ')
                    add(item)
                    display_dashboard()
                    ...
                case '2':
                    print('editing...')
                    display_dashboard()
                    ...
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
                    ...
                case '4':
                    print('completing an item')
                    while True:
                        num = int(input("Change Done status for item #?: "))
                        if num not in range(1, len(todos)):
                            print(f'Please enter a valid number (1-{len(todos)})')
                        elif num == 'exit':
                            break
                        else:
                            complete()
                            display_dashboard()
                    ...
                case '5':
                    os.system('clear')
                    show_table()
                    print('exiting...')
                    sys.exit()
                    ...       
            ...

def add(title):
    global todos
    item = Todo(title)
    todos.append(str(item))

def display_dashboard():
    os.system('clear')
    print("........")
    show_table()
    print("........")
    print("""Options
          1. Add
          2. Edit
          3. Remove
          4. Complete
          5. Exit
          """)
    ...


def show_table():
    print('----Table----')
    if todos:
        print(todos)
    else:
        print('---empty---')
    
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
