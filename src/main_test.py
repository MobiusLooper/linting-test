from main import add


def test_success():
    assert add(2, 2) == 4


def test_failure():
    assert add(2, 3) == 4
