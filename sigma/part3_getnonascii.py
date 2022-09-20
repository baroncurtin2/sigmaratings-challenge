from concurrent.futures import ProcessPoolExecutor
from typing import Iterator


def get_non_ascii(string_list: list[str]) -> list[str]:
    return [string for string in string_list if not string.isascii()] if string_list else []


def get_non_ascii_string(string: str) -> str | None:
    if not string.isascii():
        return string


def get_non_ascii_multiprocessing(string_list: list[str]) -> Iterator[str | None]:
    with ProcessPoolExecutor() as executor:
        non_ascii_strings = executor.map(get_non_ascii_string, string_list)
    return non_ascii_strings
