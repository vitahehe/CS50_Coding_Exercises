from twttr import shorten


def test_aeiou_remove():
    assert shorten('hello') == 'hll'
    assert shorten('lole')=='ll'
def test_AEIOU_remove():
    assert shorten('HELLO') == 'HLL'
    assert shorten('POLEO') =='PL'

