from calc import add, mul


def test_add() -> None:
    assert add(2, 3) == 5


def test_mul() -> None:
    assert mul(2, 3) == 6


def test_add_negative() -> None:
    assert add(-1, 1) == 0
