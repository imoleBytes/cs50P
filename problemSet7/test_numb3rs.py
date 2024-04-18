from numb3rs import validate

def test_validate_1range():
    assert validate('199.199.1.0') == True
    assert validate('127.199.1.0') == True

def test_validate_2range():
    assert validate('255.255.55.25') == True

def test_validate_invalid():
    assert validate('257.20.12.1') == False

def test_validate_first_byte():
    assert validate('1.561.876.276') == False
    assert validate('22.277.278.255') == False
