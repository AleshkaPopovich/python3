"""Lecture 01 practice problems.

Implement each function below so tests pass.
Rules:
- Do not change function names/signatures.
- Keep implementations pure unless the function explicitly needs I/O.
- Use only the Python standard library.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque


def normalize_username(name: str) -> str:
    """Return a normalized username.

    Rules:
    - Trim outer whitespace
    - Lowercase everything
    - Replace internal whitespace runs with a single underscore
    """
    return "_".join(name.strip().lower().split())


def is_valid_age(age: int) -> bool:
    """Return True if age is in [18, 120], otherwise False."""
    return 18 <= age <= 120


def truthy_values(values: list[object]) -> list[object]:
    """Return a new list containing only truthy values from input."""
    return [value for value in values if value]


def sum_until_negative(numbers: list[int]) -> int:
    """Return sum of numbers until the first negative value (exclusive)."""
    total = 0
    for number in numbers:
        if number < 0:
            break
        total += number
    return total


def skip_multiples_of_three(numbers: list[int]) -> list[int]:
    """Return numbers excluding values divisible by 3."""
    return [number for number in numbers if number % 3 != 0]


def first_even_or_none(numbers: list[int]) -> int | None:
    """Return the first even number, or None if no even number exists."""
    for number in numbers:
        if number % 2 == 0:
            return number
    return None


def squares_of_even(numbers: list[int]) -> list[int]:
    """Return squares of all even numbers in input order."""
    return [number * number for number in numbers if number % 2 == 0]


def word_lengths(words: list[str]) -> dict[str, int]:
    """Return dict mapping each word to its length."""
    return {word: len(word) for word in words}


def zip_to_pairs(keys: list[str], values: list[int]) -> list[tuple[str, int]]:
    """Zip keys and values into list of pairs. Ignore extras in longer list."""
    return list(zip(keys, values))


def build_user(name: str, role: str = "student", active: bool = True) -> dict[str, object]:
    """Build and return {'name': name, 'role': role, 'active': active}."""
    return {"name": name, "role": role, "active": active}


def append_tag_safe(tag: str, tags: list[str] | None = None) -> list[str]:
    """Append tag to tags safely (no shared mutable default across calls)."""
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


def invert_dict(mapping: dict[str, int]) -> dict[int, str]:
    """Invert mapping. Assume values are unique."""
    return {value: key for key, value in mapping.items()}


def unique_sorted_tags(tags: list[str]) -> list[str]:
    """Return unique tags sorted ascending."""
    return sorted(set(tags))


def count_words(words: list[str]) -> dict[str, int]:
    """Count occurrences of each word using collections.Counter."""
    return dict(Counter(words))


def group_scores(records: list[tuple[str, int]]) -> dict[str, list[int]]:
    """Group scores by student name using collections.defaultdict(list)."""
    grouped: defaultdict[str, list[int]] = defaultdict(list)
    for name, score in records:
        grouped[name].append(score)
    return dict(grouped)


def rotate_queue(items: list[str], steps: int) -> list[str]:
    """Rotate queue to the right by `steps` using collections.deque and return as list."""
    queue = deque(items)
    queue.rotate(steps)
    return list(queue)


def safe_int(value: str) -> int | None:
    """Convert string to int, returning None if conversion fails."""
    try:
        return int(value)
    except ValueError:
        return None


def read_lines(path: str) -> list[str]:
    """Read a text file with a context manager and return non-empty stripped lines."""
    with open(path, encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def top_n_scores(scores: list[int], n: int = 3) -> list[int]:
    """Return top `n` scores in descending order."""
    return sorted(scores, reverse=True)[:n]


def all_passed(scores: list[int], threshold: int = 50) -> bool:
    """Return True if every score is >= threshold."""
    return all(score >= threshold for score in scores)
