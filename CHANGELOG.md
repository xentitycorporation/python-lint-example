# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2025-11-10] - Environment Configuration and Testing Improvements

### Added
- **Environment variable configuration**: Caesar cipher shift now configurable via `SHIFT` environment variable
- **`.env` file support**: Added python-dotenv dependency for loading configuration from `.env` file
- **Configuration template**: Added `.env.example` with default shift value of 4
- **Enhanced test coverage**: New tests for different shift values using environment variable mocking
- **Module reload testing**: Tests use `importlib.reload()` to verify environment configuration changes
- AI development support with comprehensive Copilot instructions in `.github/copilot-instructions.md`
- Documentation chat mode configuration in `.github/chatmodes/document.chatmode.md`
- Detailed AI coding agent instructions covering:
  - Project architecture and patterns
  - Testing methodologies for interactive CLI applications
  - Environment variable configuration patterns
  - Linting configuration and CI/CD workflows
  - Development setup and commands
- This CHANGELOG.md to track project changes

### Changed
- **Shift configuration**: Moved from hard-coded `shift = 3` to environment variable `SHIFT` with fallback default of 3
- **Default shift value**: New installations use shift=4 via `.env` file
- **Dependencies**: Added python-dotenv to dev-requirements.txt for .env file support
- **Git ignore**: Properly exclude `.env` files from version control
- Updated README.md with configuration instructions and examples
- Enhanced testing documentation with environment variable testing patterns
- Updated Copilot instructions to reflect new configuration approach
- Improved development workflow documentation with configuration steps

## Previous Development

### Initial Implementation
- Basic Caesar cipher encoding/decoding functionality
- Google Python Style Guide compliance via `.pylintrc`
- GitHub Actions CI/CD pipeline with linting and testing
- Comprehensive multi-tool linting setup (Black, isort, mypy, pycodestyle, pydocstyle, vulture)
- Interactive CLI interface for encoding/decoding
- Full test coverage with pytest and coverage reporting