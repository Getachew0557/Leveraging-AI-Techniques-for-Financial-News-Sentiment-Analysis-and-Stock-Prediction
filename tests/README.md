# Tests

This directory is intended for unit tests and integration tests for the project. Testing ensures that the scripts and models function as expected and that new changes do not introduce bugs.

## How to Use

1. Add test scripts to this directory following the naming convention `test_<functionality>.py`.
2. Run the tests using a testing framework like `unittest` or `pytest`.

    ```bash
    pytest tests/
    ```

3. Review the test results to ensure all tests pass successfully.

## Best Practices

- Write tests for each new feature or function.
- Ensure tests are independent and do not rely on external state.
- Aim for high code coverage to catch potential bugs early.
