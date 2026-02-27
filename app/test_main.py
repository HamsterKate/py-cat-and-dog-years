from app.main import get_human_age


def test_should_return_zero_when_both_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_ages_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_ages_equal_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_not_increment_when_between_15_and_23() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_ages_equal_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_increment_correctly_after_24() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_calculate_large_numbers_correctly() -> None:
    assert get_human_age(100, 100) == [21, 17]
