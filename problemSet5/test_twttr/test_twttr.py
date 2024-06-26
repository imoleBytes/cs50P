from twttr import shorten
import pytest

def test_shorten():
    assert shorten('twitter') == 'twttr'
    assert shorten('hello') == 'hll'


def test_shorten_empty_str():
    assert shorten('') == ''

def test_shorten_capital_argurment():
    assert shorten('CAPITAL') == 'CPTL'

def test_shorten_lower_argurment():
    assert shorten('lower') == 'lwr'

def test_shorten_number():
    with pytest.raises(TypeError):
        shorten(56)
