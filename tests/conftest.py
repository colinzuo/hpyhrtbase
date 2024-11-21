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


@pytest.fixture(scope="session")
def proj_test_dir(root_dir) -> str:
    target = os.path.join(root_dir, "proj_test")
    return target


@pytest.fixture(autouse=True)
def hpyhrt_context_reset():
    yield
    hpyhrt_context.reset()


@pytest.fixture(autouse=True)
def init_app_base_reset():
    yield
    init_app_base.reset()


@pytest.fixture
def init_app():
    # tests_dir = os.path.dirname(__file__)
    # config_file = os.path.join(tests_dir, "run_zhiyoufy_worker.conf")
    # init_app_base.init_app_base(config_file, init_app_default_configs)

    # global_context = zhiyoufy_context.get_global_context()
    pass


@pytest.fixture
def config_inst(init_app):
    # return zhiyoufy_context.get_config_inst()
    pass
