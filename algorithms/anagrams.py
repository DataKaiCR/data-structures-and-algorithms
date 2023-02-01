
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
from helper import benchmark, logger


class IsAnagram:

    def __init__(self, word1: str, word2: str) -> None:
        assert type(word1) == str, 'Anagrams only work for strings!'
        assert type(word2) == str, 'Anagrams only work for strings!'
        self.word1 = word1
        self. word2 = word2


    def base_case(self) -> True:
        # If the words differ from length then we don't need to do compute anything else.
        if len(self.word1) != len(self.word2):
            return True

    @logger
    @benchmark
    def compute_by_hash(self) -> bool:
        if self.base_case() is None:
            freq1 = {}
            freq2 = {}

            for letter in self.word1:
                freq1[letter] = (self.word1.count(letter))

            for letter in self.word2:
                freq2[letter] = (self.word2.count(letter))

            if freq1 == freq2:
                return True
        return False

    @logger
    @benchmark
    def compute_by_counter(self) -> bool:
        if self.base_case() is None:
            return Counter(self.word1) == Counter(self.word2)
        
    @logger
    @benchmark
    def compute_by_sorting(self) -> bool:
        if self.base_case() is None:
            return sorted(self.word1) == sorted(self.word2)
        
