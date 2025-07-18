# test_main.py

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unittest.mock import patch
from io import StringIO

from main import decode, encode, main


def test_encode():
    assert encode("hey") == "khB"


def test_decode():
    assert decode('khB') == 'hey'

def test_main_encode():
    """Test main function with encode choice"""
    with patch('builtins.input', side_effect=['encode', 'hello']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue().strip()
            # 'hello' encoded should be 'khoor'
            assert output == 'khoor'


def test_main_decode():
    """Test main function with decode choice"""
    with patch('builtins.input', side_effect=['decode', 'khoor']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue().strip()
            # 'khoor' decoded should be 'hello'
            assert output == 'hello'


def test_main_with_spaces():
    """Test main function handles spaces correctly"""
    with patch('builtins.input', side_effect=['encode', 'hello world']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue().strip()
            # 'hello world' encoded should preserve the space
            assert 'khoor zruog' == output
