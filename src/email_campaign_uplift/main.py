from email_campaign_uplift.data import load_hillstrom_data
from email_campaign_uplift.data import get_metric_group_sizes
from email_campaign_uplift.stats import srm_check
from email_campaign_uplift.stats import z_test_two_proportion

treament_group = "Womens E-Mail"
control_group = "No E-Mail"
metric_col = 'visit'
group_col = 'segment'
expected_shares = [1/3, 1/3, 1/3]

if __name__ == "__main__":
    data = load_hillstrom_data("data/hillstrom_data.csv")
    obs_counts = data["segment"].value_counts()
    p_value_srm = srm_check(obs_counts, expected_shares)
    print(f"the p_value for the SRM returned by the chisquare goodness of fit test is: {p_value_srm}")
    if p_value_srm < 0.5:
        print("SRM likely. You should stop the process and find the root cause")
    group_sizes = get_metric_group_sizes(data, group_col, metric_col)
    print("#"*80)
    print("GROUP SIZES")
    print("#*80")
    print(group_sizes)
    print("#"*80)
    success_t = group_sizes.loc[treament_group, 'sum']
    success_c = group_sizes.loc[control_group, 'sum']
    size_t = group_sizes.loc[treament_group, 'count']
    size_c = group_sizes.loc[control_group, 'count']
    success_t_rate = group_sizes.loc[treament_group, 'mean']
    success_c_rate = group_sizes.loc[control_group, 'mean']
    print("Perform a one sided two-proportion z test; a positive z means treatment success rate is higher")
    print(f"The treatment success rate was", success_t_rate)
    print(f"The control success rate was", success_c_rate)
    print(f"The difference in the two rates was", {round(success_t_rate-success_c_rate), 3})
    z, p_value = z_test_two_proportion(success_t, success_c, size_t, size_c)
    print(f"z_statistic is POSITIVE: {z>0}")
    print("the z statitic was", round(z, 3))
    print("the p_value from the one side two-proportioned z_test was < 0.001: ", p_value)


