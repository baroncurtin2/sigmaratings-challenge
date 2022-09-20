from sigma.part2_anagram import is_anagram, is_anagram_counter, is_anagram_dict
import pytest


@pytest.mark.parametrize(
    "first,second,expected",
    [
        ("Debit Card", "Bad Credit", True),
        ("tacoCat", "Cattaco", True),
        ("bad", "good", False),
        ("bad", "dba", True),
    ],
)
def test_is_anagram(first, second, expected):
    assert is_anagram(first, second) == expected


@pytest.mark.parametrize(
    "first,second,expected",
    [
        ("Debit Card", "Bad Credit", True),
        ("tacoCat", "Cattaco", True),
        ("bad", "good", False),
        ("bad", "dba", True),
    ],
)
def test_is_anagram_counter(first, second, expected):
    assert is_anagram_counter(first, second) == expected


@pytest.mark.parametrize(
    "first,second,expected",
    [
        ("Debit Card", "Bad Credit", True),
        ("tacoCat", "Cattaco", True),
        ("bad", "good", False),
        ("bad", "dba", True),
    ],
)
def test_is_anagram_dict(first, second, expected):
    assert is_anagram_dict(first, second) == expected
