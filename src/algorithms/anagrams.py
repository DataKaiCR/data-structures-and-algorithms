
''' The problem
        Given two strings, word1 and word2 respectively, verify that they are anagrams.
        An anagram is when two words have the same characters and frequency.
    Example
        input:
            word1 = 'nameless'
            word2 = 'salesmen'
        output:
            true
        explanation:
            - nameless and salesmen share the same characters (namels)
            - the repetition of characters (frequency) is the same:
                {n:1, a:1, m:1, e:2, l:1, s:2}
'''

from collections import Counter
from typing import Optional


class IsAnagram:
    ''' To solve this algorithm we will abide by a few ground rules:
            1. We won't accept any parameter that is not a string literal.
            2. If the lengths of the words differ they are not an anagram.
    '''

    def __init__(self, word1: str, word2: str) -> None:
        assert isinstance(word1, str), 'Anagrams only work for strings!'
        assert isinstance(word2, str), 'Anagrams only work for strings!'
        self.word1 = word1
        self. word2 = word2

    def base_case(self) -> bool:
        # If the words differ from length then we don't need to do compute anything else.
        if len(self.word1) != len(self.word2):
            return True
        return False

    def compute_by_hash(self) -> bool:
        if self.base_case() is False:
            freq1 = {}
            freq2 = {}

            for letter in self.word1:
                freq1[letter] = (self.word1.count(letter))

            for letter in self.word2:
                freq2[letter] = (self.word2.count(letter))

            if freq1 == freq2:
                return True
        return False

    def compute_by_counter(self) -> Optional[bool]:
        return Counter(self.word1) == Counter(self.word2) if self.base_case() is False else None

    def compute_by_sorting(self) -> Optional[bool]:
        return sorted(self.word1) == sorted(self.word2) if self.base_case() is False else None
