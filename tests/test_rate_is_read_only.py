import pytest

from email_campaign_uplift.groups import GroupResult


def test_rate_readonly():
    treatmentgroup = GroupResult(1000, 10000)
    with pytest.raises(AttributeError):
        treatmentgroup.rate = 0.05

    