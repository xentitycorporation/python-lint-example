# Copilot Instructions for Python Lint Example

## Project Overview
This is a simple Caesar cipher implementation demonstrating Python linting and testing best practices. The core functionality provides encoding/decoding with a fixed shift of 3 characters.

## Key Architecture
- **main.py**: Single-file application with `encode()`, `decode()`, and interactive `main()` functions
- **Character set**: Uses `string.ascii_letters + string.punctuation + string.digits` (not just alphabet)
- **Global variables**: `shift = 3` and `letters` are module-level constants used by encode/decode functions
- **Space handling**: Spaces are preserved as-is during encoding/decoding operations

## Testing Patterns
- Tests use `sys.path.insert(0, ...)` pattern to import from parent directory without packages
- Mock `builtins.input` and `sys.stdout` for testing interactive `main()` function
- Example test structure:
  ```python
  with patch('builtins.input', side_effect=['encode', 'hello']):
      with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
          main()
          assert mock_stdout.getvalue().strip() == 'khoor'
  ```

## Development Workflow
- **Install deps**: `pip install -r dev-requirements.txt`
- **Run tests**: `python -m pytest tests/ --cov=main`
- **Run manually**: `python main.py` for interactive mode
- **Coverage**: Tests require coverage reporting; PR comments show coverage via GitHub Actions

## Linting Configuration
- Uses Google Python Style Guide via `.pylintrc`
- GitHub Actions runs comprehensive linting on push:
  - Black (formatting), isort (imports), mypy (types)
  - pycodestyle (--max-line-length=88), pydocstyle (docstrings)
  - vulture (dead code detection)
  - **Note**: pylint disabled, flake8 disabled in favor of pycodestyle
- Linting targets `./tests/*.py` specifically, not main.py

## CI/CD Behavior
- **On push**: Comprehensive linting (lint.yml)
- **On PR**: Test execution with coverage reporting (test.yml)
- Coverage comments automatically added to PRs via `coroo/pytest-coverage-commentator`

## Code Patterns
- Module docstring at top: `"""Example module for linting and testing"""`
- Functions lack type hints (pre-typing adoption)
- String concatenation used instead of f-strings or join()
- Global scope usage for configuration (shift, letters)
- No error handling for invalid characters in encode/decode