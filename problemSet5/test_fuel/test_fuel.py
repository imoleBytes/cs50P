from fuel import convert, gauge
import pytest


def test_convert_():
    assert convert('1/4') == 25
    assert convert("3/5") == 60

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
        convert("8/0")

def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert('4/7/9')
        convert('7/4')
        convert('78')
        convert('hello world')

def test_convert_empty_str():
    with pytest.raises(ValueError):
        convert('')

def test_gauge():
    assert gauge(convert('1/4')) == '25%'
    assert gauge(convert('3/5')) == '60%'

def test_gauge_full():
    assert gauge(convert('99/100')) == 'F'

def test_gauge_Empty():
    assert gauge(convert('1/100')) == 'E'

def test_gauge_typeerror():
    with pytest.raises(TypeError):
        gauge('')



