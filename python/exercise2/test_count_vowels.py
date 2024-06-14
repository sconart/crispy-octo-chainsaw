import pytest
from .count_vowels import count_vowels


@pytest.mark.parametrize(
    "input_str, expected_count",
    [
        ("hello", 2),
        ("world", 1),
        ("", 0),
        ("AEIOU", 5),
        ("python", 1),
        ("beautiful", 5),
        ("rhythm", 0),
        ("aeiouAEIOU", 10),
        ("quick brown fox", 4),
    ],
)
def test_count_vowels(input_str, expected_count):
    assert count_vowels(input_str) == expected_count


if __name__ == "__main__":
    input_str = input("Enter a string: ")
    print(f"Number of vowels: {count_vowels(input_str)}")
