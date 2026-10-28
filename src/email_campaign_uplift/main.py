from email_campaign_uplift.data import load_hillstrom_data
from email_campaign_uplift.stats import srm_check

if __name__ == "__main__":
    data = load_hillstrom_data("data/hillstrom_data.csv")
    obs_counts = data["segment"].value_counts()
    expected_shares = [1/3, 1/3, 1/3]
    srm = srm_check(obs_counts, expected_shares)
    print(obs_counts)
    print(srm)

