# test_main.py

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unittest.mock import patch
from io import StringIO

from main import decode, encode, main


def test_encode():
    # With shift=4 (from .env), 'hey' becomes 'li}'
    assert encode("hey") == "li}"


def test_decode():
    # With shift=4 (from .env), 'li}' decodes back to 'hey'
    assert decode('li}') == 'hey'

def test_main_encode():
    """Test main function with encode choice"""
    with patch('builtins.input', side_effect=['encode', 'hello']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue().strip()
            # With shift=4, 'hello' encoded should be 'lipps'
            assert output == 'lipps'


def test_main_decode():
    """Test main function with decode choice"""
    with patch('builtins.input', side_effect=['decode', 'lipps']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue().strip()
            # With shift=4, 'lipps' decoded should be 'hello'
            assert output == 'hello'


def test_main_with_spaces():
    """Test main function handles spaces correctly"""
    with patch('builtins.input', side_effect=['encode', 'hello world']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue().strip()
            # With shift=4, 'hello world' encoded should preserve the space
            assert 'lipps ${vph' == output


def test_encode_with_custom_shift():
    """Test encoding with different shift values using environment variable"""
    with patch.dict(os.environ, {'SHIFT': '5'}):
        # Force reimport to pick up new environment variable
        import importlib
        import main
        importlib.reload(main)
        
        # With shift=5, 'a' should become 'f'
        assert main.encode("a") == "f"
        assert main.encode("hello") == "mjqqt"


def test_decode_with_custom_shift():
    """Test decoding with different shift values using environment variable"""
    with patch.dict(os.environ, {'SHIFT': '5'}):
        # Force reimport to pick up new environment variable
        import importlib
        import main
        importlib.reload(main)
        
        # With shift=5, 'f' should decode back to 'a'
        assert main.decode("f") == "a"
        assert main.decode("mjqqt") == "hello"


def test_main_with_custom_shift():
    """Test main function with custom shift from environment"""
    with patch.dict(os.environ, {'SHIFT': '2'}):
        with patch('builtins.input', side_effect=['encode', 'test']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                # Force reimport to pick up new environment variable
                import importlib
                import main
                importlib.reload(main)
                
                main.main()
                output = mock_stdout.getvalue().strip()
                # With shift=2, 'test' should become 'vguv'
                assert output == 'vguv'


def test_default_shift_fallback():
    """Test that default shift of 3 is used when no environment variable is set"""
    with patch.dict(os.environ, {}, clear=True):
        # Remove SHIFT from environment if it exists
        if 'SHIFT' in os.environ:
            del os.environ['SHIFT']
        
        # Force reimport to pick up cleared environment
        import importlib
        import main
        importlib.reload(main)
        
        # Should default to shift=3, so 'hello' becomes 'khoor'
        assert main.encode("hello") == "khoor"
