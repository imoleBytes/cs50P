from plates import is_valid


def test_is_valid_empty_str():
    assert is_valid('') == False

def test_is_valid_more_than_6chrs():
    assert is_valid('Ae326ndhd') == False

def test_is_valid_valid():
    assert is_valid('CS50') == True

def test_is_valid_middle_number():
    assert is_valid('AS23EG') == False

def test_is_valid_begin_with_number():
    assert is_valid('2BGAS7') == False

def test_is_valid_less_2chars():
    assert is_valid('S') == False

def test_is_valid_starts_with_char():
    assert is_valid('SE6556') == True

def test_is_valid_starts_without_nonchar():
    assert is_valid('-$BSWE') == False

def test_is_valid_zero_placement():
    assert is_valid('SE056') == False

def test_is_valid_no_non_alphanum():
    assert is_valid('SE. 56') == False
