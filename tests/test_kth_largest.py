import pytest
from algorithms import KthLargest


def test_class_instance() -> None:
    obj = KthLargest([1], 0)
    assert isinstance(obj, KthLargest)


@pytest.mark.parametrize("input1, input2, expected", [
    ([], 0, 'Your array must contain at least 1 number'),
    ([1], -1, 'Your k value must be a positive integer')
])
def test_class_instance_fail_by_empty_array_or_k_value(input1, input2, expected) -> None:
    with pytest.raises(AssertionError) as context:
        KthLargest(arr=input1, k=input2)
    assert (expected in str(context.value))


def test_base_case() -> None:
    obj1 = KthLargest([1], 0)
    obj2 = KthLargest([5], 6)
    assert (obj1.base_case() == obj1.arr[0])
    assert (obj2.base_case() == obj2.arr[0])


def test_compute_kth() -> None:
    obj = KthLargest([0, 2, 3, 7, 5, 6, 7], 4)
    assert (obj.compute_kth() == 5)


def test_compute_kth_fail() -> None:
    obj = KthLargest(['1','2'], 3)
    assert (obj.compute_kth() is None)


def test_compute_kth_with_heap() -> None:
    obj = KthLargest([0, 2, 3, 7, 5, 6, 7], 4)
    assert (obj.compute_kth_with_heap() == 5)


def test_compute_kth_with_heap_fail() -> None:
    obj = KthLargest(['1','2'], 3)
    assert (obj.compute_kth_with_heap() is None)
