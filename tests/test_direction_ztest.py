#a test for one sided two proportion z test where the treatment success rate is clearly lower

import pytest

from email_campaign_uplift.stats import z_test_two_proportion

success_t = 150
success_c = 500
size_t = 1000
size_c = 1000



def test_z_negative():
    z, _ = z_test_two_proportion(success_t, success_c, size_t, size_c)
    assert z < 0

def test_p_near_1():
    _, p_value = z_test_two_proportion(success_t, success_c, size_t, size_c)
    assert p_value == pytest.approx(1)