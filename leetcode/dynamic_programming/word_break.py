'''
Leetcode #139: Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    n = len(wordDict)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]
