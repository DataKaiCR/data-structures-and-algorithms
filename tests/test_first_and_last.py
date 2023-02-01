import pytest
from algorithms import FirstAndLast

def test_class_instance() -> None:
    obj = FirstAndLast([1], 0)
    assert isinstance(obj, FirstAndLast)

def test_class_instance_fail_by_non_array() -> None:
    with pytest.raises(AssertionError) as context:
        obj = FirstAndLast('x', 0)
    assert ('You must supply an array' in str(context.value))

def test_class_instance_fail_by_wrong_target() -> None:
    with pytest.raises(AssertionError) as context:
        obj = FirstAndLast([1], 'y')
    assert ('Your target must be a positive integer' in str(context.value))