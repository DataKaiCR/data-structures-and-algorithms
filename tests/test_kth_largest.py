import pytest
from algorithms import KthLargest


def test_class_instance() -> None:
    obj = KthLargest([1], 0)
    assert isinstance(obj, KthLargest)


def test_class_instance_fail_by_empty_array() -> None:
    with pytest.raises(AssertionError) as context:
        KthLargest([], 0)
    assert ('Your array must contain at least 1 number' in str(context.value))


def test_class_instance_fail_by_k() -> None:
    with pytest.raises(AssertionError) as context:
        KthLargest([1], -1)
    assert ('Your k value must be a positive integer' in str(context.value))


def test_base_case() -> None:
    obj1 = KthLargest([1], 0)
    obj2 = KthLargest([5], 6)
    assert (obj1.base_case() == obj1.arr[0])
    assert (obj2.base_case() == obj2.arr[0])


def test_compute_kth() -> None:
    obj = KthLargest([0, 2, 3, 7, 5, 6, 7], 4)
    assert (obj.compute_kth() == 5)


def test_compute_kth_with_heap() -> None:
    obj = KthLargest([0, 2, 3, 7, 5, 6, 7], 4)
    assert (obj.compute_kth_with_heap() == 5)
