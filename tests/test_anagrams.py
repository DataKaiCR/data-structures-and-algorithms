import pytest
from algorithms import IsAnagram


def test_class_instance() -> None:
    obj = IsAnagram('hello', 'friend')
    assert isinstance(obj, IsAnagram)


@pytest.mark.parametrize("input1, input2, expected", [
    ([], 0, 'Anagrams only work for strings'),
    ('init', 1, 'Anagrams only work for strings'),
    (True, 'story', 'Anagrams only work for strings')
])
def test_not_a_word(input1, input2, expected) -> None:
    with pytest.raises(AssertionError) as context:
        IsAnagram(word1=input1, word2=input2)
    assert (expected in str(context.value))


def test_base_case() -> None:
    obj = IsAnagram('my', 'bad')
    assert (obj.base_case() is True)


def test_compute_by_hash_true() -> None:
    obj = IsAnagram('dog', 'god')
    assert obj.compute_by_hash() is True


def test_compute_by_hash_false() -> None:
    obj = IsAnagram('happy', 'times')
    assert obj.compute_by_hash() is False


def test_compute_by_counter_true() -> None:
    obj = IsAnagram('dog', 'god')
    assert obj.compute_by_counter() is True


def test_compute_by_counter_false() -> None:
    obj = IsAnagram('happy', 'times')
    assert obj.compute_by_counter() is False


def test_compute_by_sorting_true() -> None:
    obj = IsAnagram('dog', 'god')
    assert obj.compute_by_sorting() is True


def test_compute_by_sorting_false() -> None:
    obj = IsAnagram('happy', 'times')
    assert obj.compute_by_sorting() is False
