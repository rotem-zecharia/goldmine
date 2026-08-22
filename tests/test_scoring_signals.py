from goldmine.scoring import (
    contributor_signal,
    issue_close_signal,
    recency_signal,
    star_signal,
    velocity_signal,
)

TODAY = "2026-08-22"


def test_star_signal_is_log_scaled_not_linear():
    low, mid, high = star_signal(200), star_signal(2_000), star_signal(20_000)

    assert low < mid < high
    assert round(mid - low, 5) == round(high - mid, 5)


def test_star_signal_saturates_at_the_top():
    assert star_signal(200_000) == 1.0


def test_star_signal_of_zero_is_zero():
    assert star_signal(0) == 0.0


def test_recency_signal_is_full_for_a_push_today():
    assert recency_signal("2026-08-22", today=TODAY) == 1.0


def test_recency_signal_decays_with_age():
    assert recency_signal("2026-07-23", today=TODAY) > recency_signal("2026-02-22", today=TODAY)


def test_recency_signal_bottoms_out_after_a_year():
    assert recency_signal("2024-01-01", today=TODAY) == 0.0


def test_contributor_signal_rewards_a_real_team():
    assert contributor_signal(1) < contributor_signal(3) < contributor_signal(10)


def test_contributor_signal_saturates():
    assert contributor_signal(50) == 1.0


def test_issue_close_signal_is_the_closed_ratio():
    assert issue_close_signal(open_issues=1, closed_issues=9) == 0.9


def test_issue_close_signal_is_neutral_with_no_issues():
    assert issue_close_signal(open_issues=0, closed_issues=0) == 0.5


def test_velocity_signal_is_none_when_velocity_is_unknown():
    assert velocity_signal(None) is None


def test_velocity_signal_rewards_growth():
    assert velocity_signal(0.0) < velocity_signal(50.0) < velocity_signal(500.0)


def test_velocity_signal_treats_star_loss_as_zero():
    assert velocity_signal(-10.0) == 0.0
