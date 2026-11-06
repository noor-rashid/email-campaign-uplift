from email_campaign_uplift.stats import calculate_lift
import pytest

success_t = 100
success_c = 100
size_t = 1000
size_c = 1000

def test_equal_lift():
    assert calculate_lift(success_t, success_c, size_t, size_c) == (0.0, 0.0)