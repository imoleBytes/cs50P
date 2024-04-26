




class Todo:
    ID = 0
    """This clss represent a todo"""
    def __init__(self, title: str, done=False) -> None:
        self.title = title
        self.done = done
        self.id = Todo.ID + 1
        Todo.ID = self.id
    
    def __str__(self) -> str:
        return f"#{self.id}- Title: {self.title}, Done: {self.done}"

    def to_dict(self):
        return str(self.__dict__)

    @classmethod
    def total_todos(cls):
        return cls.ID
    
    ...




if __name__ == "__main__":
        
    print('Total todos before: ', Todo.total_todos())

    todo1 = Todo('1 todo')

    print(todo1)
    print(todo1.id)
    print(todo1.to_dict())
    print('Total todos after: ',Todo.total_todos())

