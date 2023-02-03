
''' The problem
        Given an array of integers arr and an integer k, find the kth largest element.
    Example
        input:
            arr = [1,2,5,7,9]
            k = 4
        output:
            2
        explanation:
            - 1st largest # is 9
            - 2nd largest # is 7
            - 3rd largest # is 5
            - 4th largest # is 2
'''

import heapq
from typing import Optional, List


class KthLargest:

    def __init__(self, arr: List[int], k: int) -> None:
        # We want our object instantiation to fail if the following contraints are not met. Doing so prevents any further computation.
        # Method 1
        assert len(arr) > 0, 'Your array must contain at least 1 number'
        assert k >= 0, 'Your k value must be a positive integer'
        self.arr = arr
        self.k = k
        # Method 2
        # We can also use ValueErrors, they are less pythonic so we won't use them but keep in mind assert methods could be disabled by the user with python -O
        #         # if k < 0:
        #     raise ValueError('Your k value must be a positive integer')
        # if len(arr) < 1:
        #     raise ValueError('Your array must contain at least 1 number')
        # else:
        #     self.arr = arr
        #     self.k = k

    def base_case(self) -> Optional[int]:
        # We want a method to handle all bases cases to avoid unnecesary computation.
        return self.arr[0] if len(self.arr) == 1 or self.k > len(self.arr) else None
            

    def compute_kth(self) -> Optional[int]:
        # Easy method by sorting the array and then returning the k index by using the end of the array as the starting point.
        # We avoid using the reverse() method as it's additional computation.
        if self.base_case() is None:
            return sorted(self.arr)[-self.k]
        return None

    def compute_kth_with_heap(self) -> Optional[int]:
        if not self.base_case():
            self.arr = [-x for x in self.arr]
            heapq.heapify(self.arr)
            for i in range(self.k-1):
                heapq.heappop(self.arr)
            return -heapq.heappop(self.arr)
        return None
