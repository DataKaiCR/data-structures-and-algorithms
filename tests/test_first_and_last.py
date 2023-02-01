import pytest
from algorithms import FirstAndLast


def test_class_instance() -> None:
    obj = FirstAndLast([1], 0)
    assert isinstance(obj, FirstAndLast)


@pytest.mark.parametrize("input1, input2, expected", [
    ('x', 0, 'You must supply an array'),
    ([1], 'y', 'Your target must be a positive integer')
])
def class_instance_fail_by_nonvalid_parameters(input1, input2, expected) -> None:
    with pytest.raises(AssertionError) as context:
        FirstAndLast(word1=input1, word2=input2)
    assert (expected in str(context.value))
