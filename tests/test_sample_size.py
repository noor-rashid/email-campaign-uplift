

from email_campaign_uplift.stats import sample_size_two_proportion


def test_sample_size_known_value():
    p_c = 0.10
    mde = 0.02

    assert sample_size_two_proportion(p_c, mde) == 3026

def test_sample_size_more_power_needs_more_people():
    p_c = 0.10
    mde = 0.02
    power = 0.9

    assert sample_size_two_proportion(p_c, mde, power=power) == 4191

def test_sample_size_stricter_alpha_needs_more_people():
    p_c = 0.10
    mde = 0.02
    alpha = 0.01

    assert sample_size_two_proportion(p_c, mde, alpha) == 4912

def test_sample_size_returns_int():
    p_c = 0.10
    mde = 0.02
    assert type(sample_size_two_proportion(p_c, mde)) is int
