# python-lint-example
An example of a simple Python script with comprehensive linting and testing setup, demonstrating best practices for Python development workflows.

## Functionality
This project implements a Caesar cipher with a fixed shift of 3 characters, providing:
- **Encoding**: Converts plain text to encoded text
- **Decoding**: Converts encoded text back to plain text  
- **Character support**: Works with letters, punctuation, and digits (preserves spaces)
- **Interactive mode**: Run `python main.py` for an interactive encoding/decoding session

### Example Usage
```bash
$ python main.py
would you like to encode or decode? encode
Please enter text: hello world
khoor zruog
```

## Development Setup
Install development dependencies:
```bash
pip install -r dev-requirements.txt
```

Run tests with coverage:
```bash
python -m pytest tests/ --cov=main
```

## Linting
Comprehensive linting is set up automatically on [GitHub Actions](.github/workflows/lint.yml) using multiple tools:
- **Black** for code formatting
- **isort** for import sorting  
- **mypy** for type checking
- **pycodestyle** for PEP 8 compliance (max line length: 88)
- **pydocstyle** for docstring conventions
- **vulture** for dead code detection

Configuration follows [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) via [`.pylintrc`](.pylintrc).

## Testing
Automated testing runs on [GitHub Actions for pull requests](.github/workflows/test.yml):
- **pytest** for test execution
- **pytest-cov** for coverage reporting
- **Automatic coverage comments** on PRs via `coroo/pytest-coverage-commentator`

Tests include comprehensive scenarios:
- Basic encode/decode functionality
- Interactive main function testing with mocked input/output
- Space preservation verification
- Located in [`tests/test_main.py`](tests/test_main.py)

## AI Development Support
This project includes configuration for AI coding assistants:
- **Copilot Instructions**: Comprehensive guidelines for AI agents in [`.github/copilot-instructions.md`](.github/copilot-instructions.md)
- **Documentation Chat Mode**: Automated documentation assistance in [`.github/chatmodes/document.chatmode.md`](.github/chatmodes/document.chatmode.md)
