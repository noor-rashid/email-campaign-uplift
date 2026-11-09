import pytest

from email_campaign_uplift.groups import GroupResult


def test_groupsize_rate():
    treatment = GroupResult(1000, 10000)
    assert treatment.rate == pytest.approx(0.1)
