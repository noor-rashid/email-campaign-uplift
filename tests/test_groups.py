import pytest

from email_campaign_uplift.groups import GroupResult


def test_class_value_error():
    
    with pytest.raises(ValueError):
        _ = GroupResult(5, 0)
    
def test_groupsize_rate():
    treatment = GroupResult(1000, 10000)
    assert treatment.rate == pytest.approx(0.1)

def test_rate_readonly():
    treatmentgroup = GroupResult(1000, 10000)
    with pytest.raises(AttributeError):
        treatmentgroup.rate = 0.05