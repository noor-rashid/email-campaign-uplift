import pytest

from email_campaign_uplift.stats import bootstrap_ci_diff, calculate_lift, wald_ci_diff


def test_bootstrap_same_seed_same_result():
    success_t = 120
    success_c = 100
    size_t = 1000
    size_c = 1000

    assert bootstrap_ci_diff(success_t, success_c, size_t, size_c, n_boot=2000, seed=1) == bootstrap_ci_diff(success_t, success_c, size_t, size_c, n_boot=2000, seed=1)

def test_bootstrap_different_seed_differs():
    success_t = 120
    success_c = 100
    size_t = 1000
    size_c = 1000

    assert bootstrap_ci_diff(success_t, success_c, size_t, size_c, n_boot=2000, seed=1) != bootstrap_ci_diff(success_t, success_c, size_t, size_c, n_boot=2000, seed=2)

def test_bootstrap_close_to_wald():
    success_t = 120
    success_c = 100
    size_t = 1000
    size_c = 1000

    assert bootstrap_ci_diff(success_t, success_c, size_t, size_c) == pytest.approx(wald_ci_diff(success_t, success_c, size_t, size_c), abs=0.003)

def test_bootstrap_contains_lift():
    success_t = 120
    success_c = 100
    size_t = 1000
    size_c = 1000
    abs, _ = calculate_lift(success_t, success_c, size_t, size_c)
    lower, upper = bootstrap_ci_diff(success_t, success_c, size_t, size_c, n_boot=2000) 
    assert lower < abs < upper