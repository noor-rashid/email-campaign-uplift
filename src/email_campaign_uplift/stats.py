import numpy as np
from scipy.stats import norm
from scipy.stats import chisquare
from email_campaign_uplift.data import get_metric_group_sizes


def srm_check(obs_counts: list[int], expected_shares: list[float]) -> float:
    """performing a chisquare goodness of fit test to check SRM"""
    total_users = sum(obs_counts)
    expected = [i*total_users for i in expected_shares]
    chi = chisquare(f_obs=obs_counts, f_exp=expected)
    return chi[1]

def z_test_two_proportion(success_t: int, success_c: int, size_t: int, size_c: int) -> tuple[float, float]:
    """performs a two-proportion z test"""
    p1 = success_t/size_t
    p2 = success_c/size_c
    total_size = size_t+size_c
    p_pooled = (success_t+success_c)/total_size
    pooled_p1 = p_pooled*(1-p_pooled)
    pooled_p1_div = pooled_p1/size_t
    pooled_p2_div = pooled_p1/size_c
    pooled_addition = pooled_p1_div + pooled_p2_div
    se_ztest = np.sqrt(pooled_addition)
    point_estimate = p1-p2
    z_first = (point_estimate - 0)
    z = z_first / se_ztest
    auc = norm.sf(z)
    return (z, auc)