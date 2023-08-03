from pytest_proj.utils.arrs import my_slice, get


def test_get():
    assert get([1, 2, 3], 1, "test") == 2
    assert get([], -1, "test") == "test"


def test_slice():
    assert my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert my_slice([1, 2, 3], 1) == [2, 3]
