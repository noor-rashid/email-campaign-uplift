from scipy.stats import chisquare
import pandas as pd
from typing import List

def hillstrom_srm_check(obs_counts: List[int], expected_shares: List[float]) -> float:
    total_users = sum(obs_counts)
    expected = [i*total_users for i in expected_shares]
    chi = chisquare(f_obs=obs_counts, f_exp=expected)
    return chi[1]

