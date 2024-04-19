import pytest
from working import convert


def test_convert_raise_valueError():
    with pytest.raises(ValueError):
        convert('9:00 AM - 5:00 PM')

def test_convert_with_min():
    assert convert('9:35 AM to 5:20 PM') == '09:35 to 17:20'

def test_convert_without_min():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'

def test_convert_invalid_time():
    with pytest.raises(ValueError):
        convert('13 PM to 5 PM')

def test_convert_12AM():
    assert convert('12:10 AM to 5 PM') == '00:10 to 17:00'

def test_convert_12PM():
    assert convert('12:10 PM to 5 PM') == '12:10 to 17:00'
