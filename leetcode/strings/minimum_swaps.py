'''
Leetcode #1247: Minimum Swaps to Make Strings Equal

You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. 
Your task is to make these two strings equal to each other. You can swap any two characters that belong 
to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.
'''

def minimumSwap(s1: str, s2: str) -> int:

        x_y_diff = 0
        y_x_diff = 0
        
        for i in range(len(s1)):
            if s1[i] == "x" and s2[i] == "y":
                x_y_diff += 1
            elif s1[i] == "y" and s2[i] == "x":
                y_x_diff += 1

        if (x_y_diff + y_x_diff) % 2 != 0:
            return -1
            
        return (x_y_diff // 2) + (y_x_diff // 2) + (x_y_diff % 2) * 2