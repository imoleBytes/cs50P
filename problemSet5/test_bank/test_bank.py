from bank import value


def test_value_starts_with_hello():
    assert value('hello') == 0
    assert value('hello world') == 0

def test_value_starts_with_h():
    assert value('help') == 20
    assert value('heap') == 20

def test_value_starts_otherwise():
    assert value('chulo') == 100
    assert value('dave') == 100


