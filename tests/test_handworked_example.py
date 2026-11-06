from email_campaign_uplift.stats import calculate_lift
import pytest

success_t = 100
success_c = 200
size_t = 1000
size_c = 1000

def test_handworked_example():
    assert calculate_lift(success_t, success_c, size_t, size_c) == (-0.1, -0.5)