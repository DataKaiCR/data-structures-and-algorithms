import logging
from time import perf_counter
from typing import Callable, Any
from functools import wraps

def logger(original_func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(original_func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logging.info(f'Executing {original_func.__name__}')
        result = original_func(*args, **kwargs)
        logging.info(f'Finished executing {original_func.__name__}')
        return result

    return wrapper