import numpy as np
from scipy.stats import chisquare, norm


def srm_check(obs_counts: list[int], expected_shares: list[float]) -> float:
    """performing a chisquare goodness of fit test to check SRM"""
    total_users = sum(obs_counts)
    expected = [i*total_users for i in expected_shares]
    chi = chisquare(f_obs=obs_counts, f_exp=expected)
    return chi[1]

def z_test_two_proportion(success_t: int, success_c: int, size_t: int, size_c: int) -> tuple[float, float]:
    """one sided two-proportion z_test: tests whether treatment success rate is higher than 
    the control success rate.

    uses a pooled standard error undr the null hypothesis (p_t == p_c). The z_statistic
    is (p_t - p_c)/se, so a positive z means that treatment is higher
    
    Args: 
        success_t: #number of successes in treatment group
        success_c:  #number of successes in control group
        size_t:  #size of the treatment group
        size_c: #size of the control group

    Returns:
        (z, p_value) as floats. p_value is the upper tail area
        
    """
    #point estimates for the success rate for each group
    p_t = success_t/size_t  
    p_c = success_c/size_c 

    #pooled proportion. best estimate of the shared rate under H0
    p_pooled = (success_t+success_c)/(size_t+size_c) 

    #pooled standard error of the differene: sqrt(p*(1-p)*(1/size_t + 1/size_c))
    pooled_variance = p_pooled*(1-p_pooled) 
    se = np.sqrt(pooled_variance * (1/size_t+1/size_c))
    
    #test stat, observed difference divided by the standard error under h0
    z = (p_t - p_c) / se
    
    #one sided pval, probability of a z at least this large under h0
    p_value = norm.sf(z) 
    
    return (z, p_value) 



def calculate_lift(success_t: int, success_c: int, size_t: int, size_c: int) -> tuple[float, float]:
    """
    calculates the absolute and relative lift between the two variants.

    Args:
        success_t: int, number of successes in treatment
        success_c: int, number of successes in control
        size_t: int, total size of treatment
        size_c: int, total size of control

    Returns:
        absolute_lift: float, fraction, difference between treatment and control
        relative_lift: float, fraction, change between treatment and control

    """

    p_t = success_t / size_t 
    p_c = success_c / size_c

    abs_lift = p_t - p_c
    rel_lift = (p_t-p_c)/p_c

    return abs_lift, rel_lift

def wald_ci_diff(success_t, success_c, size_t, size_c, alpha=0.05) -> tuple[float, float]:
    """
    creates 95% confidence interval. unpooled. two-sided
    
    Args:
        success_t: int, number of successes in treatment
        success_c: int, number of successes in control
        size_t: int, total size of treatment
        size_c: int, total size of control
        alpha: float, significance level

    Returns:
        lower: float
        upper: float
    """
    #point estimates
    p_t = success_t / size_t
    p_c = success_c / size_c
    diff = p_t - p_c

    #standard error
    variance_t = p_t*(1-p_t)
    variance_c = p_c*(1-p_c)
    se = np.sqrt(variance_t/size_t + variance_c/size_c)

    #confidence intervals at 95%
    alpha = alpha/2
    critical_val = norm.ppf(1-alpha)

    upper = diff + critical_val * se
    lower = diff - critical_val * se
    

    return lower, upper