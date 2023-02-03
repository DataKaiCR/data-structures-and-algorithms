
''' The problem
        Given an n value, find the respective fibonacci number from the sequence that corresponds to n.
    Example:
        input:
            n = 5
        output:
            5
        explanation:
            - Taking an array of length 6 of fibonacci numbers is [0,1,1,2,3,5]
            - F(0) = 0
            - F(1) or F(2) = 1
            - F(3) = 2
            - F(4) = 3
            - F(5) = 5
    Authors Notes:
        I wanted to use a recurssion algorithm so naturally the old and reliable Fibonacci numbers came into mind.

        However, I do want to point out that while recurssion is a good technique it has its limitations.
        Calling a function itself a number of times can add up pretty quickly if its not used properly.
        That is why I think this is such a good example to learn about dynamic programming and its benefits.

        For this problem I could have just made a standard class and added each technique as it's own method,
        but I felt like doing it a bit differently and using other tools and options we have available
        when creating and instantiating objects.
'''

from abc import ABC, abstractmethod
from typing import Optional


class Fibonacci(ABC):
    ''' When thinking about a Fibonacci object we can imagine a hash that when calling its index[n]
        it will return the corresponding fibonacci number.

        We know for certain that the first 3 numbers (We also want to include 0 as a valid option)
        are 0,1,1. So we use that as our base case and any other class that inherits from Fibonacci
        must include that information.

        Another aspect or constraint of this Fibonacci object is that it can only
        calculate positive fibonacci numbers. Since we are using recurssion mostly we want our object
        to call itself instead of a method, so we also want all our Fib classes to contain a __call___ method
        instantiation. This call method will check that only positive integers are given.
    '''
    @abstractmethod
    def __init__(self) -> None:
        self.memo = {0: 0, 1: 1, 2: 1}
        pass

    @abstractmethod
    def __call__(self, n: int) -> Optional[int]:
        assert isinstance(n, int) and n >= 0, f'You can only call positive numbers, got {n}'
        return None


class SlowFibonacci(Fibonacci):
    ''' Why is this method so slow?
        Well, by applying recurssion we call our function an n number of times by each n value. Since we
        are doing two separate calculations (n - 1) and (n - 2) that means that we are calling ourselves
        a 2 ** n number of times. So because we are dealing with exponentials, this means
        the time will increment drastically for each larger number we provided as input.
        This is called time complexity. (0)

        So basically if we were to find out the 50th Fib number, our time complexity would be
        O(2**n) which is 2 ** 50 calculations! That is over 4 quadrillion steps.
    '''

    def __init__(self) -> None:
        super().__init__()

    def __call__(self, n: int) -> int:
        super().__call__(n)
        if n in self.memo:
            return self.memo[n]
        return self(n - 1) + self(n - 2)


class MemoFibonacci(Fibonacci):
    ''' Why is this method much faster if it's also recurssive?
        As you can tell we are doing pretty much the same, except this time we are taking advantage of
        our previously created dictionary and now we are saving each computation into our hash.

        Welcome to dynamic programming.
        By storing each calculation in a dictionary, once we run into a similar situation, we won't need
        to compute it again. We save ourselves this trouble because we already did it before!
        This is called memoization.

        Now, our time complexity has been reduced from 0(2**n) to 0(n)
    '''

    def __init__(self) -> None:
        super().__init__()

    def __call__(self, n):
        super().__call__(n)
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self(n - 1) + self(n - 2)
        return self.memo[n]


class IterativeFibonacci(Fibonacci):
    ''' Wasn't our memoized recurssion algorithm good enough?
        Well, not quite. While it is way much better, you will start to notice that if the input is too
        big our virtual memory will start to suffer.

        So we pivot into iterations. By using iterable unpacking, we can use a very memory efficient algorithm
        for each computation during the for loop. Whoever told you for loops are bad is not completely off,
        but should take the time and learn a bit more.
    '''

    def __init__(self) -> None:
        super().__init__()

    def __call__(self, n):
        super().__call__(n)
        if n == 0:
            return self.memo[0]
        previous_fib, current_fib = self.memo[0], self.memo[1]
        for _ in range(2, n + 1):
            previous_fib, current_fib = current_fib, previous_fib + current_fib
        return current_fib
