from email_campaign_uplift.data import load_hillstrom_data
from email_campaign_uplift.stats import srm_check

treament_group = "WOMEN'S EMAIL"
control_group = "NO EMAIL"
metric_col = 'visit'
group_col = 'segment'
expected_shares = [1/3, 1/3, 1/3]

if __name__ == "__main__":
    data = load_hillstrom_data("data/hillstrom_data.csv")
    obs_counts = data["segment"].value_counts()
    chi = srm_check(obs_counts, expected_shares)
    if chi[1] > 0.5:
        print("SRM likely. Stop process")
    


