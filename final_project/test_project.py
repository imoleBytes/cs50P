from project import *

def test_add():
    add("some data")
    assert todos[-1].title == 'some data'

def test_remove():
    if todos:
        initial_len = len(todos)
        add("data")
        add("data")
        add("data")
        remove(todos, 1)
        remove(todos, 1)
        remove(todos, 1)
        assert len(todos) == initial_len

def test_display_dashboard():
    assert display_dashboard() == None

def test_persist_data():
    add('last data')
    persist_data()
    with open("data.json", "r") as f:
        ls = json.load(f)
    assert ls[-1]["title"] == "last data"
