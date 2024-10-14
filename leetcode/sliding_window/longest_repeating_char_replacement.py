'''
Leetcode #424 
'''

def characterReplacement(s: str, k: int) -> int:
        l = 0
        res = 1

        char_map = {s[l]: 1}
        most_char = 0
        for r in range(1, len(s)):
            char_map[s[r]] = char_map.get(s[r], 0) + 1
            most_char = max(most_char, char_map[s[r]])
            if (r - l + 1) - most_char <= k:
                res = max(res, r - l + 1)
            else:
                char_map[s[l]] -= 1
                l += 1
        return res