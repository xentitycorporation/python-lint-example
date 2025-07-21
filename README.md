# python-lint-example
An example of a simple python script with linting and testing setup.

## Linting
Linting is setup automatically on [github actions via pylint](.github/workflows/lint.yml).
Our configuration file was taken from [google best practices](https://google.github.io/styleguide/pyguide.html).


## Testing
Testing is setup automatically on [github actions with pytest on PRs](.github/workflows/test.yml).
This also reports the code coverage, of which minimums can be set to succeed/fail the tests.
This forces developers to write new tests for new functions/code/use cases and keep the code hardened.

The tests themselves are defined in [test_main.py](test_main.py). Simple verifications that the
functions are working as expected.
