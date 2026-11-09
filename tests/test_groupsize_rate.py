import pytest
from email_campaign_uplift.groups import GroupResult

treatment = GroupResult(1000, 10000)

def test_groupsize_rate():
    assert treatment.rate == pytest.approx(0.1)
