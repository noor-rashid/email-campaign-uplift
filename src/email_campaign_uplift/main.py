from email_campaign_uplift.data import get_metric_group_sizes, load_hillstrom_data
from email_campaign_uplift.stats import srm_check, z_test_two_proportion

treatment_group = "Womens E-Mail"
control_group = "No E-Mail"
metric_col = 'visit'
group_col = 'segment'
expected_shares = [1/3, 1/3, 1/3]
srm_alpha = 0.001
z_test_alpha = 0.05

if __name__ == "__main__":
    data = load_hillstrom_data("data/hillstrom_data.csv")
    obs_counts = data[group_col].value_counts()
    p_value_srm = srm_check(obs_counts, expected_shares)
    print(f"the p_value for the SRM returned by the chisquare goodness of fit test is: {p_value_srm}")
    if p_value_srm < srm_alpha:
        print("SRM likely. You should stop the process and find the root cause")
    group_sizes = get_metric_group_sizes(data, group_col, metric_col)
    print("#"*80)
    print("GROUP SIZES".center(78))
    print("#"*80)
    print(group_sizes)
    print("#"*80)
    success_t = group_sizes.loc[treatment_group, 'sum']
    success_c = group_sizes.loc[control_group, 'sum']
    size_t = group_sizes.loc[treatment_group, 'count']
    size_c = group_sizes.loc[control_group, 'count']
    success_t_rate = group_sizes.loc[treatment_group, 'mean']
    success_c_rate = group_sizes.loc[control_group, 'mean']
    print("Perform a one sided two-proportion z test; a positive z means treatment success rate is higher")
    print("The treatment success rate was", round(success_t_rate, 3)*100,"%")
    print("The control success rate was", round(success_c_rate,3)*100,"%")
    print("The difference in the two rates was", round(success_t_rate-success_c_rate, 3)*100,"pct points")
    z, p_value = z_test_two_proportion(success_t, success_c, size_t, size_c)
    print(f"z_statistic is POSITIVE: {z>0}")
    print("the z statitic was", round(z, 3))
    if p_value < z_test_alpha: 
        print("the p_value from the one side two-proportioned z_test was < 0.001: ", p_value < 0.001)
        print(f"p_value (area under the curve for upper tail) was < 0.001, smaller than our alpha of {z_test_alpha}")
        print("We can therefore reject the null hyptothesis in favour of the alternative hypothesis that the treatment increases the true visit rate")
    else:
        print("p_value greater than our stated alpha", p_value, z_test_alpa)
        print("therefore, we fail to reject the null hypothesis that there is no difference between treatment and control ")
