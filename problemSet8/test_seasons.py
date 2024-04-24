import pytest
from seasons import validate_date



def test_validate_date_invalid():
    assert validate_date('Jan 1, 2004') == False

def test_validate_date_valid():
    assert validate_date('2004-01-01') == True
