import pytest
from email_campaign_uplift import GroupResult



def test_class_value_error():
    
    with pytest.raises(ValueError):
        treatment = GroupResult(5, 0)
    print("Size cannot be 0")
