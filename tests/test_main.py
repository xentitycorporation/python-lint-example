# test_main.py

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import decode, encode


def test_encode():
    assert encode("hey") == "khB"


def test_decode():
    assert decode("khB") == "hey"
