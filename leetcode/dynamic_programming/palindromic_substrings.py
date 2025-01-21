'''
Leetcode #643 Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
'''


def countSubstrings(s: str) -> int:
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    count = 0

    for i in range(n):
        dp[i][i] = True
        count += 1

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            count += 1

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i - 1][j + 1]:
                dp[i][j] = True
                count += 1

    return count
