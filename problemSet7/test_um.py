import pytest
from um import count


# def test_count():
#     with pytest.raises(ValueError):
#         count('9:00 AM - 5:00 PM')

def test_count_within_word():
    assert count('yummy') == 0

def test_count():
    assert count('hello, um, you!') == 1

# def test_count_uppercase():
#     with pytest.raises(ValueError):
#         count('13 PM to 5 PM')

def test_count_uppercase():
    assert count('hello Um') == 1

# def test_count_12PM():
#     assert count('12:10 PM to 5 PM') == '12:10 to 17:00'
