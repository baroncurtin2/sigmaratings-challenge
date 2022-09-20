import re
from collections import Counter, defaultdict


def is_anagram(first: str, second: str) -> bool:
    """Time O(nlogn) / O(1) memory complexity"""
    if len(first) != len(second):
        return False

    first_, second_ = anagram_test_formatter(first), anagram_test_formatter(second)

    return sorted(first_) == sorted(second_)


def is_anagram_counter(first: str, second: str) -> bool:
    """Time O(n) / O(1) memory complexity"""
    if len(first) != len(second):
        return False

    first_, second_ = anagram_test_formatter(first), anagram_test_formatter(second)

    return Counter(first_) == Counter(second_)


def is_anagram_dict(first: str, second: str) -> bool:
    """Time O(n) and O(n) memory complexity"""
    if len(first) != len(second):
        return False

    counts = defaultdict(int)
    first_, second_ = anagram_test_formatter(first), anagram_test_formatter(second)

    for c1, c2 in zip(first_, second_):
        counts[c1] += 1
        counts[c2] -= 1

    return all(v == 0 for v in counts.values())


def anagram_test_formatter(word: str) -> str:
    pattern = r"^\s+|\s+$|\s+"
    return re.sub(pattern, "", word.lower())
