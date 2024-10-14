'''
Leetcode #566
'''

def checkInclusion(s1: str, s2: str) -> bool:
        # Check if a permutation is possible
        if len(s2) < len(s1):
            return False

        # Put s1 into a map of char and count
        s1_chars = {}
        for char in s1:
            s1_chars[char] = s1_chars.get(char, 0) + 1

        # Set up window map
        window_chars = {}
        for i in range(len(s1)):
            window_chars[s2[i]] = window_chars.get(s2[i], 0) + 1

        # Check if intial maps are equal
        if s1_chars == window_chars:
            return True

        # Move sliding window and return true if the maps are equal
        l = 0
        for r in range(len(s1), len(s2)):
            window_chars[s2[r]] = window_chars.get(s2[r], 0) + 1
            window_chars[s2[l]] = window_chars.get(s2[l], 1) - 1
            if window_chars[s2[l]] == 0:
                window_chars.pop(s2[l])
            l += 1
            if window_chars == s1_chars:
                return True


        return False
