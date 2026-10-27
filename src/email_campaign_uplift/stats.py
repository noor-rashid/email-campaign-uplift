from scipy.stats import chisquare
import pandas as pd


def hillstrom_srm_check(data: pd.DataFrame) -> float:
    """performs a sample ratio mismatch via chisquare test of independence"""
    observed = data["segment"].value_counts()
    total_users = sum(observed)
    expected = [total_users/3, total_users/3, total_users/3]
    chi_stat = chisquare(observed, f_exp=expected)
    return chi_stat[1]