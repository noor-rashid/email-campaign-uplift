from collections.abc import Sequence

import numpy as np
import pytest
from statsmodels.stats.proportion import proportions_ztest

from email_campaign_uplift.stats import z_test_two_proportion

count = np.array([3238, 2262])
nobs = np.array([21387, 21306])
alternative = 'larger'

success_t = count[0]
success_c = count[1]
size_t = nobs[0]
size_c = nobs[1]



def statsmodels_prop_ztest(
    count: Sequence[int],
    nobs: Sequence[int],
    alternative: str
) -> tuple[float, float]:
    """
    uses the statsmodels python library to perform a test for proportions based on a normal (z) test

    count: number of successes in nobs trials. if an array, represents successes in each group
    nobs: the number of trials, the same length as count

    alternative(str): larger means treatment is larger than control

    returns:
    z test statistic and p_value
    """

    stat, pval = proportions_ztest(count, nobs, alternative=alternative)

    return stat, pval

def test_ztest_functions():
    assert z_test_two_proportion(success_t, success_c, size_t, size_c) == pytest.approx(statsmodels_prop_ztest(count, nobs, alternative))