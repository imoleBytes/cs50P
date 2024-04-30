
"""This module contains the Todo class"""

class Todo:
    """This clss represent the todo blueprint"""
    def __init__(self, title: str, done=False) -> None:
        self.title = title
        self.done = done
    
    def __str__(self) -> str:
        return f"Title: {self.title}, Done: {self.done}"

    def to_dict(self):
        return (self.__dict__)
