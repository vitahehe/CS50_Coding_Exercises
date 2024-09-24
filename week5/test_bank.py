from bank import value

def test_first():
    assert value('hello')== 0

def test_second():
    assert value('hey')== 20

def test_third():
    assert value('bonjours') == 100
    assert value('BONJOURS') == 100

