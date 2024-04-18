from numb3rs import validate

def test_validate_1range():
    assert validate('199.199.1.0') == True
    assert validate('127.199.1.0') == True

def test_validate_2range():
    assert validate('255.255.55.25') == True

def test_validate_invalid():
    assert validate('257.20.12.1') == False


