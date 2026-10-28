
from scipy.stats import chisquare


def srm_check(obs_counts: list[int], expected_shares: list[float]) -> float:
    """performing a chisquare goodness of fit test to check SRM"""
    total_users = sum(obs_counts)
    expected = [i*total_users for i in expected_shares]
    chi = chisquare(f_obs=obs_counts, f_exp=expected)
    return chi[1]

