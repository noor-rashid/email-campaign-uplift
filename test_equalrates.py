# What happens if the two variants have equal rates?
#In this case the expectation is clear. Z would be exactly 0 since the top part
#of the equation is p_t-p_c = 0
from email_campaign_uplift.stats import z_test_two_proportion

success_t = 100
success_c = 100
size_t = 1000
size_c = 998

def test_ztest_equal():
    """this test would pass if test_stat, z, is exactly 0"""
    assert z_test_two_proportion(success_t, success_c, size_t, size_c) == 0