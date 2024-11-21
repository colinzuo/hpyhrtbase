
## package layout

[https://github.com/pypa/sampleproject](https://github.com/pypa/sampleproject)

### src

使用src目录可以方面同时支持测试installed和dev版本

[https://docs.pytest.org/en/stable/explanation/goodpractices.html#tests-outside-application-code](https://docs.pytest.org/en/stable/explanation/goodpractices.html#tests-outside-application-code)

- Your tests can run against an installed version after executing `pip install .`
- Your tests can run against the local copy with an editable install after executing `pip install --editable .`

## pytest

测试通过pytest

[https://docs.pytest.org/en/stable/getting-started.html](https://docs.pytest.org/en/stable/getting-started.html)

[https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-discovery](https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-discovery)

[https://docs.pytest.org/en/stable/how-to/mark.html](https://docs.pytest.org/en/stable/how-to/mark.html)

[https://docs.pytest.org/en/stable/how-to/assert.html](https://docs.pytest.org/en/stable/how-to/assert.html)

pytest will run all files of the form `test_*.py or *_test.py` in the current directory and its subdirectories.

```bash
pytest test_mod.py

pytest testing/

pytest test_mod.py::test_func

pytest test_mod.py::TestClass::test_method

pytest -m slow
```
