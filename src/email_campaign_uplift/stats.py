import numpy as np
from scipy.stats import chisquare, norm
from statsmodels.stats.proportion import proportions_ztest


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



def statsmodels_prop_ztest(count: int, nobs: int, alternative: str) -> tuple[float, float]:
    """
    def statsmodels_z_proportion_test(count: int, nobs: int, value: float) -> tuple[float, float]:

    uses the statsmodels python library to perform a test for proportions based on a normal (z) test

    count: number of successes in nobs trials. if an array, represents successes in each group
    nobs: the number of trials, the same length as count

    alternative(str): larger means prop > value (default value is 0)

    returns:
    z test statistic and p_value
    """

    stat, pval = proportions_ztest(count, nobs, alternative=alternative)

    return stat, pval
