import pytest

from hpyhrtbase.utils import Throttle


@pytest.fixture
def throttle_inst() -> Throttle:
    target = Throttle(
        delay_maps={
            "sina.com": 0.1,
            "jd.com": 0.2,
        }
    )
    return target


@pytest.mark.parametrize(
    "target_url, expected_effective_domain, expected_sleep_secs",
    [
        ("http://www.sina.com:80", "sina.com", 0.1),
        ("https://www.jd.com:443", "jd.com", 0.2),
    ],
)
def test_calc_wait(
    throttle_inst, target_url, expected_effective_domain, expected_sleep_secs
):
    throttle_inst.wait(target_url)
    effective_domain, sleep_secs = throttle_inst.calc_wait(target_url)

    assert effective_domain == expected_effective_domain
    assert sleep_secs == pytest.approx(expected_sleep_secs, abs=0.02)
