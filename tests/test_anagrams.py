import pytest
from algorithms import IsAnagram

def test_class_instance() -> None:
    obj = IsAnagram('hello','friend')
    assert isinstance(obj, IsAnagram)

def test_not_a_word() -> None:
    with pytest.raises(AssertionError) as context:
        obj1 = IsAnagram([], 0)
    assert ('Anagrams only work for strings' in str(context.value))
    with pytest.raises(AssertionError) as context:
        obj2 = IsAnagram('init', 1)
    assert ('Anagrams only work for strings' in str(context.value))
    with pytest.raises(AssertionError) as context:
        obj3 = IsAnagram(True, 'story')
    assert ('Anagrams only work for strings' in str(context.value))

def test_base_case() -> None:
    obj = IsAnagram('my','bad')
    assert (obj.base_case() == True)

def test_compute_by_hash_true() -> None:
    obj = IsAnagram('dog','god')
    assert obj.compute_by_hash() is True
    
def test_compute_by_hash_false() -> None:
    obj = IsAnagram('happy','times')
    assert obj.compute_by_hash() is False

def test_compute_by_counter_true() -> None:
    obj = IsAnagram('dog','god')
    assert obj.compute_by_counter() is True
    
def test_compute_by_counter_false() -> None:
    obj = IsAnagram('happy','times')
    assert obj.compute_by_counter() is False

def test_compute_by_sorting_true() -> None:
    obj = IsAnagram('dog','god')
    assert obj.compute_by_sorting() is True
    
def test_compute_by_sorting_false() -> None:
    obj = IsAnagram('happy','times')
    assert obj.compute_by_sorting() is False

