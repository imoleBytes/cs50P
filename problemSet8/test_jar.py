import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(2)
    jar.deposit(3)
    assert str(jar) == '🍪🍪🍪🍪🍪'

def test_deposit():
    jar = Jar()
    jar.deposit(4)
    jar.deposit(6)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(4)

def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.deposit(6)
    jar.withdraw(4)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.withdraw(7)

def test_init_value():
    jar = Jar(20)
    assert jar.capacity == 20

def test_init_size():
    jar = Jar()
    assert jar.size == 0

def test_init_str_value():
    with pytest.raises(ValueError):
        Jar('34')
