import logging
from time import perf_counter
from typing import Callable, Any
from functools import wraps

def benchmark(original_func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(original_func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = perf_counter()
        result = original_func(*args, **kwargs)
        end = perf_counter() - start
        logging.info(f'{original_func.__name__} {original_func.__class__.__name__} ran in {end:2f} seconds')
        return result

    return wrapper