"""
Leetcode # 191: Number of 1 Bits

Given a positive integer n, write a function that returns the number of 
set bits in its binary representation (also known as the Hamming weight).
"""


def hammingWeight(n: int) -> int:

    binary = bin(n).replace("0b", "")

    count = 0
    for i in range(len(binary)):
        if binary[i] == "1":
            count += 1
        
 
    return count 