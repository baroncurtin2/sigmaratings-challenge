import itertools


def count_transformations(first: str, second: str) -> int:
    n_lcs = find_longest_common_substring_length(first, second)
    return min(len(first) - n_lcs, len(second) - n_lcs)


def find_longest_common_substring_length(first, second):
    n_f, n_s = len(first), len(second)

    dp = [[0 for _ in range(n_s + 1)] for _ in range(n_f + 1)]
    max_length = 0

    for i, j in itertools.product(range(1, n_f + 1), range(1, n_s + 1)):
        dp[i][j] = 1 + dp[i - 1][j - 1] if first[i - 1] == second[j - 1] else max(dp[i - 1][j], dp[i][j - 1])

        max_length = max(max_length, dp[i][j])

    return max_length
