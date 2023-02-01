''' The problem
        Given a sorted array of integers arr and an integer target, find the index of the first and last position of target in arr.
        If target can't be found in arr, return [-1,-1]
    Example
        input:
            arr = [0,1,1,2]
            target = 1
        output:
            [1,2]
        explanation:
            - the first 1 in the array is in position 1: arr[1] = 1
            - the last 1 in the array is in position 2: arr[2] = 1
'''

from typing import List


class FirstAndLast:

    def __init__(self, arr: List[int], target: int) -> None:
        assert isinstance(arr, list), 'You must supply an array'
        assert isinstance(target, int), 'Your target must be a positive integer'
        self.arr = sorted(arr)
        self.target = target

    def compute_by_iteration(self) -> List[int]:
        # Go until each item in the array until we find a match. If no match we default to [-1,-1]
        for i in range(len(self.arr)):
            # Match found
            if self.arr[i] == self.target:
                start = i
                # Keep incrementing the array index + 1 until the target is different from value
                while i + 1 < len(self.arr) and self.arr[i + 1] == self.target:
                    i += 1
                return [start, i]
        return [-1, -1]
