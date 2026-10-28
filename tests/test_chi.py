from email_campaign_uplift.stats import srm_check

obs_counts = [100, 100]
expected_shares = [0.5, 0.5]

def test_srm_check():
    assert srm_check(obs_counts, expected_shares) == 1
