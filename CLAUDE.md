# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

hpyhrtbase is a shared Python base library providing config management, application lifecycle, logging, error models, and utilities.

## Commands

```bash
# Setup (using uv)
uv venv --python 3.12
uv pip install -r requirements-tests.txt
uv pip install -e .

# Setup (using pip)
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Unix
pip install -r requirements-tests.txt
pip install -e .

# Run all tests
pytest

# Run a single test file
pytest tests/test_config.py

# Run a single test
pytest tests/test_config.py::test_params_from_file -v

# Lint
ruff check .

# Type check
mypy src
```

## Architecture

### Bootstrap Flow

`init_app_base(config_path)` is the single entry point for application initialization:
1. Locates config file via `IOUtil.find_abs_path`
2. Derives `root_dir` from config file location via `IOUtil.find_root_dir`
3. Parses HOCON config into a `Params` object (with `root_dir` injected as override)
4. Stores config in global context (`hpyhrt_context.set_config_inst`)
5. Calls optional app-specific default config callback, then `init_base_default_configs`
6. Creates a `Throttle` instance on `global_context`
7. Creates required directories (`project_dir`, `data_cache_dir`, `output_dir`)
8. Sets up logging via `setup_logging`

Guard: `init_app_base` raises if called twice. Tests reset state via `conftest.py` autouse fixtures.

### Configuration (`config.py`)

`Params` is a dict-like object with dot-notation access. Created from HOCON files via `params_from_file(config_files, overrides)`. Supports multiple config files concatenated, with string overrides appended last. Nested dicts are auto-converted to nested `Params` objects.

Default config keys set by `init_base_default_configs`: `data_dir`, `norm_timeout`, `data_cache_dir`, `output_dir`.

### Global Context (`hpyhrt_context.py`)

Module-level singletons providing dependency injection:
- `config_inst` (`Params`): accessed via `get_config_inst()` / `set_config_inst()`
- `global_context` (`SimpleNamespace`): runtime services like `throttle`
- `reset()`: clears both (used in tests)

### Error Model (`model/`)

Layered error/response pattern used by the FastAPI backend:
- `BaseResultErrorType` (IntEnum): standard error codes (0=OK, 1000s=general, 2000s=auth, 3000s=users)
- `ErrorInfo` (Pydantic): `code`, `message`, `detail`
- `ErrorInfoException`: exception carrying `ErrorInfo`, with `from_enum()` factory
- `ErrorResponse` (Pydantic): base response with optional `error: ErrorInfo`
- `CommonResult[T]` (Pydantic, Generic): extends `ErrorResponse` with `data: T | None`

Controller pattern: decorate handlers with `@FuncUtil.deco_handle_error_info_exception` to auto-catch `ErrorInfoException` and return `ErrorResponse`.

### Utilities (`utils/`)

All utility classes use static methods (no instance state). Key utilities:

- **Throttle**: Domain-based rate limiting with built-in delays for financial data sources (tushare, sina, eastmoney, etc.). Stored on `global_context.throttle`.
- **IOUtil**: File downloads, path resolution (`find_abs_path`, `find_root_dir`), directory creation, JSON/text file loading, unzip.
- **FuncUtil**: `retry` decorator (exponential backoff), `retry_until_timeout`, `deco_handle_error_info_exception`.
- **CollectionUtil**: Dict path access with dot-notation and list index support, dict merging.
- **CheckUtil**: Dict validation assertions using dot-notation paths.
- **ConfigUtil**: Sensitive config value decoding with prefix-based redirection.
- **TimeUtil**: Date int/object conversions, ISO formatting, `timeit` context manager.

### Testing

Tests use pytest with two autouse fixtures in `conftest.py`:
- `hpyhrt_context_reset`: resets global context after each test
- `init_app_base_reset`: resets init guard after each test

Test configs live in `tests/configs/`. Test output goes to `tests/proj_test/`.

## Key Conventions

- Python naming: snake_case throughout
- Utility classes: static methods only, no instance state
- Config format: HOCON (pyhocon) with `root_dir` auto-injected
- Linting: Ruff with E, W, F, I, B, C4, UP rules; E501 ignored
- All models use Pydantic BaseModel
- `src` layout with `py.typed` marker for type checking support
