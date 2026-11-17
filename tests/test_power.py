import pytest

from email_campaign_uplift.stats import simulate_power

def test_simulate_power_matches_formula():
    p_c = 0.10
    p_t = 0.12
    n_per_group = 3026

    assert simulate_power(p_c, p_t, n_per_group) == pytest.approx(0.80, abs=0.03)

def test_simulate_power_no_effect_is_alpha():
    p_c = 0.10
    p_t = 0.10
    n_per_group = 3026

    assert simulate_power(p_c, p_t, n_per_group) == pytest.approx(0.05, abs=0.02)

def test_simulate_power_fewer_people_less_power():
    p_c = 0.10
    p_t = 0.12
    n_per_group = 3026

    assert simulate_power(p_c, p_t, n_per_group) > simulate_power(p_c, p_t, n_per_group//2)