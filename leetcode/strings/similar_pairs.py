from typing import List

'''
Leetcode #2506 - Count Pairs of Similiar Strings

You are given a 0-indexed string array words.

Two strings are similar if they consist of the same characters.

For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.
'''

def similarPairs(self, words: List[str]) -> int:
        pairs = 0
        word_set_map = {}
        for index, word in enumerate(words):
            word_set = set()
            for char in word:
                word_set.add(char)
            word_set_map[index] = word_set

        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if word_set_map[i] == word_set_map[j]:
                    pairs += 1
        return pairs