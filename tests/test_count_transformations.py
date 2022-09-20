import pytest
from sigma.part4_count_transformations import count_transformations


@pytest.mark.parametrize(
    "first,second,expected",
    [
        ("sigma", "ratings", 3),
        ("football", "baseball", 4),
        ("aaab", "aabb", 1),
    ],
)
def test_count_transformations(first, second, expected):
    assert count_transformations(first, second) == expected
