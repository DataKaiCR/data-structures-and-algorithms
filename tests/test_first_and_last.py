import pytest
from algorithms import FirstAndLast


def test_class_instance() -> None:
    obj = FirstAndLast([1], 0)
    assert isinstance(obj, FirstAndLast)


@pytest.mark.parametrize("input1, input2, expected", [
    ('x', 0, 'You must supply an array'),
    ([1], 'y', 'Your target must be a positive integer')
])
def test_class_instance_fail_by_nonvalid_parameters(input1, input2, expected) -> None:
    with pytest.raises(AssertionError) as context:
        FirstAndLast(arr=input1, target=input2)
    assert (expected in str(context.value))


@pytest.mark.parametrize("input1, input2, expected", [
    ([], 0, [-1, -1]),
    ([1], 0, [-1, -1]),
    ([0], 1, [-1, -1]),
    ([1, 1, 1, 1, 1, 1, 1], 9, [-1, -1])
])
def test_base_case(input1, input2, expected):
    obj = FirstAndLast(input1, input2)
    assert obj.base_case() == expected


def test_compute_by_iteration_sorted():
    obj = FirstAndLast([1, 2, 4, 5, 5, 7, 8], 5)
    assert obj.compute_by_iteration() == [3, 4]


def test_compute_by_iteration_non_sorted():
    obj = FirstAndLast([5, 7, 2, 4, 8, 5, 1], 5)
    assert obj.compute_by_iteration() == [3, 4]


def test_compute_by_iteration_not_found():
    obj = FirstAndLast([5, 1, 1, 1, 1, 1, 1], 9)
    assert obj.compute_by_iteration() == [-1, -1]


def test_find_start():
    obj = FirstAndLast([1, 2, 4, 5, 5, 7, 8], 5)
    assert obj._find_start() == 3


def test_find_start_first_item():
    obj = FirstAndLast([1, 2, 4, 5, 5, 7, 8], 1)
    assert obj._find_start() == 0


def test_find_start_target_greaterthan_mid():
    obj = FirstAndLast([1, 2, 3, 4, 5, 6], 4)
    assert obj._find_start() == 3


def test_find_start_fail():
    obj = FirstAndLast([1, 2, 3, 4, 5, 6], 0)
    assert obj._find_start() == -1


def test_find_end():
    obj = FirstAndLast([1, 2, 4, 5, 5, 7, 8], 5)
    assert obj._find_end() == 4


def test_find_end_last_item():
    obj = FirstAndLast([1, 2, 4, 5, 5, 7, 8], 8)
    assert obj._find_end() == 6


def test_find_end_target_lessthan_mid():
    obj = FirstAndLast([1, 2, 3, 4, 5, 6], 2)
    assert obj._find_end() == 1


def test_find_end_fail():
    obj = FirstAndLast([1, 2, 3, 4, 5, 6], 7)
    assert obj._find_end() == - 1


def test_compute_by_binary_search():
    obj = FirstAndLast([1, 2, 4, 5, 5, 7, 8], 5)
    assert obj.compute_by_binary_search() == [3, 4]


def test_compute_by_binary_search_fail():
    obj = FirstAndLast([1, 2, 4, 5, 5, 7, 8], 9)
    assert obj.compute_by_binary_search() == [-1, -1]
