import numpy as np
from scipy.stats import chisquare, norm


def srm_check(obs_counts: list[int], expected_shares: list[float]) -> float:
    """performing a chisquare goodness of fit test to check SRM"""
    total_users = sum(obs_counts)
    expected = [i*total_users for i in expected_shares]
    chi = chisquare(f_obs=obs_counts, f_exp=expected)
    return chi[1]

def z_test_two_proportion(success_t: int, success_c: int, size_t: int, size_c: int) -> tuple[float, float]:
    """performs a two-proportion z test
    
    Args: 
    success_t = int #number of successes in treatment group
    success_c = int #number of successes in control group
    size_t = int #size of treatment group
    size_c = int #size of control group

    Returns z and p_value as floats
        
    """
    p1 = success_t/size_t  # compute point estimate for treatment
    p2 = success_c/size_c #compute point estimate for control
    total_size = size_t+size_c #total size of treatment and control groups combined
    p_pooled = (success_t+success_c)/total_size #calculate the pooled proportion
    pooled_p1 = p_pooled*(1-p_pooled) #step 1 of calculating the standard error
    pooled_p1_div = pooled_p1/size_t #step 2
    pooled_p2_div = pooled_p1/size_c #step 3
    pooled_addition = pooled_p1_div + pooled_p2_div #step 4
    se_ztest = np.sqrt(pooled_addition) #final important step, take square root of both sides
    point_estimate = p1-p2 #calculate the difference in proportions
    z_first = (point_estimate - 0) # step one of computing test statistic
    z = z_first / se_ztest #step 2, divide by the standard error
    p_value = norm.sf(z) # calculate the area under the curve
    return (z, p_value) #return z and p_value