
import json



class Todo:
    """This clss represent a todo"""
    def __init__(self, title: str, done=False) -> None:
        self.title = title
        self.done = done
    
    def __str__(self) -> str:
        return f"Title: {self.title}, Done: {self.done}"

    def to_dict(self):
        return str(self.__dict__)

    # @classmethod
    # def total_todos(cls):
    #     return cls.ID
    
    ...




if __name__ == "__main__":
        
    # print('Total todos before: ', Todo.total_todos())
    todos = []

    # todo1 = Todo('1 todo')

    # print(todo1)
    # print(todo1.id)
    # print(todo1.to_dict())

    with open('data.json') as f:
        temp = json.load(f)
    print(type(temp))
    for i in temp:
        todos.append(Todo(i['title'], i['done']))
    
    print(todos)
    for i in todos:
        print(i)
    # print('Total todos after: ',Todo.total_todos())

