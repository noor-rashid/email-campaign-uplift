import pytest

from email_campaign_uplift.groups import GroupResult


def test_class_value_error():
    
    with pytest.raises(ValueError):
        _ = GroupResult(5, 0)
    
