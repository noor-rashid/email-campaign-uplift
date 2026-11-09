import pytest
from statsmodels.stats.proportion import confint_proportions_2indep

from email_campaign_uplift.stats import calculate_lift, wald_ci_diff

success_t = 120
success_c = 100
size_t = 1000
size_c = 1000

def test_wald_ci_matches_statsmodels():
    assert wald_ci_diff(success_t, success_c, size_t, size_c) == pytest.approx(confint_proportions_2indep(success_t, size_t, success_c, size_c, method='wald'))

def test_wald_ci_centered_on_abs_lift():
    lower, upper = wald_ci_diff(success_t, success_c, size_t, size_c) 
    abs_lift, _ = calculate_lift(success_t, success_c, size_t, size_c)
    assert (lower+upper)/2 == pytest.approx(abs_lift)

def test_wald_ci_equal_rates_symmetric():
    success_t = 100
    success_c = 100
    size_t = 1000
    size_c = 1000
    lower, upper = wald_ci_diff(success_t, success_c, size_t, size_c) 
    assert lower, upper == (-0.0263, 0.0263)

def test_wald_ci_alpha_changes_width():
    success_t = 100
    success_c = 100
    size_t = 1000
    size_c = 1000
    assert wald_ci_diff(success_t, success_c, size_t, size_c, alpha=0.01) == pytest.approx(confint_proportions_2indep(success_t, size_t, success_c, size_c, alpha=0.01, method='wald'))
