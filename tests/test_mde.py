import pytest

from email_campaign_uplift.stats import mde_two_proportion


def test_mde_round_trip():
    p_c = 0.10
    n_per_group = 3026

    assert mde_two_proportion(p_c, n_per_group) == pytest.approx(0.02, abs=0.0002)

def test_mde_more_people_smaller_mde():
    p_c = 0.10
    n_per_group = 3026
    result_a = mde_two_proportion(p_c, n_per_group)
    result_b = mde_two_proportion(p_c, n_per_group*4)
    
    assert result_b < result_a



