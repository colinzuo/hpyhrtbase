import os

import pytest

from hpyhrtbase import hpyhrt_context, init_app_base


@pytest.fixture(scope="session")
def root_dir() -> str:
    cur_file_dir = os.path.dirname(__file__)
    return cur_file_dir


@pytest.fixture(scope="session")
def configs_dir(root_dir) -> str:
    target = os.path.join(root_dir, "configs")
    return target


@pytest.fixture(autouse=True)
def hpyhrt_context_reset():
    yield
    hpyhrt_context.reset()


@pytest.fixture(autouse=True)
def init_app_base_reset():
    yield
    init_app_base.reset()
