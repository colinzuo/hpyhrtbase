
## ide

可以用vscode开发

### ruff

ruff同时支持lint和format功能

[https://docs.astral.sh/ruff/editors/setup/](https://docs.astral.sh/ruff/editors/setup/)

下面的配置是从fastapi拷贝的

```toml
[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4",  # flake8-comprehensions
    "UP",  # pyupgrade
]
ignore = [
    "E501",  # line too long, handled by black
    "B008",  # do not perform function calls in argument defaults
    "C901",  # too complex
    "W191",  # indentation contains tabs
]
```

### mypy

不确定别人是怎么用mypy的，fastapi之类的配置文件里有mypy相关配置，但mypy的官方
文档没有说怎么与editor集成

[Mypy Type Checker](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker)

## venv

```bash
python -m venv .venv
```

### windows

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

.\.venv\Scripts\activate
```

## development

```bash
pip install -e .
```

## test

[https://docs.pytest.org/en/stable/getting-started.html](https://docs.pytest.org/en/stable/getting-started.html)

```bash
pip install -r requirements-tests.txt
```
