"""Lecture 03 practice problems.

Implement each class/function below so tests pass.
Rules:
- Do not change names/signatures.
- Use only the Python standard library.

Problems:
1. Countdown iterator
2. Step iterator
3. Unique consecutive iterator
4. Circular iterator
6. File word reader generator
7. Batch generator
8. Recursive flatten generator (optional)
9. log_calls decorator
10. measure_time decorator
11. count_calls decorator
12. ensure_non_negative decorator
13. retry decorator (optional)
14. lru_cache decorator (optional)
"""

from __future__ import annotations

import time
from collections import OrderedDict
from collections.abc import Callable, Iterable, Iterator, Sequence
from functools import update_wrapper, wraps
from typing import Any


class Countdown:
    """Problem 1. Countdown iterator.

    Build an iterator class that starts at `n` and yields down to `0` inclusive.

    Example:
    >>> list(Countdown(3))
    [3, 2, 1, 0]
    """

    def __init__(self, n: int) -> None:
        self.n = n

    def __iter__(self) -> Iterator[int]:
        current = self.n
        while current >= 0:
            yield current
            current -= 1


class StepIterator:
    """Problem 2. Step iterator.

    Iterate through a list by taking every `step`-th element.
    Default `step` is `2`.
    Raise `ValueError` when `step <= 0`.

    Example:
    >>> list(StepIterator([10, 20, 30, 40, 50, 60]))
    [10, 30, 50]
    >>> list(StepIterator([1, 2, 3, 4, 5, 6, 7], step=3))
    [1, 4, 7]
    """

    def __init__(self, values: list[Any], step: int = 2) -> None:
        if step <= 0:
            raise ValueError("step must be positive")
        self.values = values
        self.step = step

    def __iter__(self) -> Iterator[Any]:
        index = 0
        while index < len(self.values):
            yield self.values[index]
            index += self.step


class UniqueConsecutiveIterator:
    """Problem 3. Unique consecutive iterator.

    Yield values while removing only *consecutive* duplicates.

    Example:
    >>> list(UniqueConsecutiveIterator([1, 1, 2, 2, 2, 3, 1, 1]))
    [1, 2, 3, 1]
    """

    def __init__(self, values: list[Any]) -> None:
        self.values = values

    def __iter__(self) -> Iterator[Any]:
        for n in range(len(self.values)):
            if n == 0 or self.values[n] != self.values[n - 1]:
                yield self.values[n]


class CircularIterator:
    """Problem 4. Circular iterator.

    Return exactly `k` values by cycling through `sequence`.
    Raise `ValueError` when sequence is empty or when `k < 0`.

    Example:
    >>> list(CircularIterator(["A", "B", "C"], 8))
    ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B']
    """

    def __init__(self, sequence: Sequence[Any], k: int) -> None:
        if not sequence or k < 0:
            raise ValueError("invalid sequence or k")
        self.sequence = sequence
        self.k = k

    def __iter__(self) -> Iterator[Any]:
        index = 0
        while index < self.k:
            yield self.sequence[index % len(self.sequence)]
            index += 1


def _flatten_values(data: list[Any]) -> Iterator[Any]:
    for item in data:
        if isinstance(item, list):
            yield from _flatten_values(item)
        else:
            yield item


class FlattenIterator:
    """Problem 5 (optional). Flatten iterator.

    Build an iterator class that yields scalar values from nested lists
    of arbitrary depth.

    Example:
    >>> list(FlattenIterator([1, [2, 3], [4, [5, 6]], 7]))
    [1, 2, 3, 4, 5, 6, 7]
    """

    def __init__(self, data: list[Any]) -> None:
        self._values = list(_flatten_values(data))
        self._index = 0

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        if self._index >= len(self._values):
            raise StopIteration
        value = self._values[self._index]
        self._index += 1
        return value

def read_words(filename: str) -> Iterator[str]:
    with open(filename, encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                yield word

"""Problem 6. File word reader generator.

    Yield one word at a time from a text file without loading the whole
    file into memory.

    Example:
    >>> list(read_words("sample.txt"))
    ['one', 'two', 'three']
    """
    

        
    


def batch(iterable: Iterable[Any], size: int) -> Iterator[list[Any]]:
    """Problem 7. Batch generator.

    Yield lists containing at most `size` items from `iterable`.
    Raise `ValueError` when `size <= 0`.

    Example:
    >>> list(batch([1, 2, 3, 4, 5, 6, 7], 3))
    [[1, 2, 3], [4, 5, 6], [7]]
    """
    if size <= 0:
        raise ValueError("size must be positive")

    current_batch: list[Any] = []
    for item in iterable:
        current_batch.append(item)
        if len(current_batch) == size:
            yield current_batch
            current_batch = []
    if current_batch:
        yield current_batch


def flatten(data: list[Any]) -> Iterator[Any]:
    """Problem 8 (optional). Recursive flatten generator.

    Recursively yield all scalar values from a nested list.

    Example:
    >>> list(flatten([1, [2, 3], [4, [5, 6]], 7]))
    [1, 2, 3, 4, 5, 6, 7]
    """
    yield from _flatten_values(data)


def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 9. `log_calls` decorator.

    Print each function call in this format:
    `name(arg1, arg2, kw=value) -> result`

    Hint:
    - Function name: `func.__name__`
    - Positional values: `args`
    - Keyword names/values: `kwargs.items()`

    Example:
    >>> @log_calls
    ... def add(a, b):
    ...     return a + b
    >>> add(2, 3)
    add(2, 3) -> 5
    5
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        parts = [repr(arg) for arg in args]
        parts.extend(f"{key}={value!r}" for key, value in kwargs.items())
        print(f"{func.__name__}({', '.join(parts)}) -> {result!r}")
        return result

    return wrapper


def measure_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 10. `measure_time` decorator.

    Measure function execution time and print:
    `Executed in <milliseconds> ms`

    Example:
    >>> @measure_time
    ... def work():
    ...     return "done"
    >>> work()
    done
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        started = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - started) * 1000
        print(f"Executed in {elapsed_ms:.3f} ms")
        return result

    return wrapper


def count_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 11. `count_calls` decorator.

    Count how many times the wrapped function is called.
    Store the counter in `wrapper.calls`.

    Example:
    >>> @count_calls
    ... def ping():
    ...     return "ok"
    >>> ping(); ping()
    'ok'
    >>> ping.calls
    2
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def ensure_non_negative(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 12. `ensure_non_negative` decorator.

    Raise `ValueError` when the decorated function returns a negative number.

    Example:
    >>> @ensure_non_negative
    ... def diff(a, b):
    ...     return a - b
    >>> diff(5, 2)
    3
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        if result < 0:
            raise ValueError("negative result is not allowed")
        return result

    return wrapper


def retry(times: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Problem 13 (optional). `retry(times)` decorator.

    Retry a function up to `times` retries after the initial attempt.
    Raise `ValueError` when `times < 0`.

    Example:
    >>> @retry(2)
    ... def flaky():
    ...     ...
    """
    if times < 0:
        raise ValueError("times must be non-negative")

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times:
                        raise
            raise RuntimeError("unreachable")

        return wrapper

    return decorator


def lru_cache(maxsize: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Problem 14 (optional). `lru_cache(maxsize)` decorator factory.

    Implement cache with Least Recently Used eviction policy.
    Keep only the last `maxsize` used results.
    Solve this one using a class.

    Example:
    >>> @lru_cache(2)
    ... def square(x):
    ...     return x * x
    >>> square(2), square(3), square(2)
    (4, 9, 4)
    """
    if maxsize < 0:
        raise ValueError("maxsize must be non-negative")

    class CachedCallable:
        def __init__(self, func: Callable[..., Any]) -> None:
            self.func = func
            self.cache: OrderedDict[tuple[Any, ...], Any] = OrderedDict()
            update_wrapper(self, func)

        def __call__(self, *args: Any, **kwargs: Any) -> Any:
            if maxsize == 0:
                return self.func(*args, **kwargs)

            key = (args, tuple(sorted(kwargs.items())))
            if key in self.cache:
                self.cache.move_to_end(key)
                return self.cache[key]

            result = self.func(*args, **kwargs)
            self.cache[key] = result
            if len(self.cache) > maxsize:
                self.cache.popitem(last=False)
            return result

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        return CachedCallable(func)

    return decorator
