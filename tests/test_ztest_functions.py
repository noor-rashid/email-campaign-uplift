from email_campaign_uplift.stats import z_test_two_proportion
from email_campaign_uplift.stats import statsmodels_prop_ztest

count = [3238, 2262]
nobs = [21387, 21306]
alternative = 'larger'

success_t = 3238
success_c = 2262
size_t = 21387
size_c = 21306

def test_ztest_functions():
    assert z_test_two_proportion(success_t, success_c, size_t, size_c) == approx statsmodels_prop_ztest(count, nobs, alternative)