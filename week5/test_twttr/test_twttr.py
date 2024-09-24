from twttr.twttr import shorten


def test_aeiou_remove():
    assert shorten('hello') == 'hll'
    assert shorten('lole')=='ll'
def test_AEIOU_remove():
    assert shorten('HELLO') == 'HLL'
    assert shorten('POLEO') =='PL'
def test_numbers():
    assert shorten('hello1') == 'hll1'
def test_punct():
    assert shorten('hello!!!')=='hll!!!'
