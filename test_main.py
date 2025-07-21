# test_main.py

from main import encode, decode

def test_encode():
    assert encode('hey') == 'khB'

def test_decode():
    assert decode('khB') == 'hey'