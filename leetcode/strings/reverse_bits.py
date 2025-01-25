"""
Leetcode #190: Reverse Bits

Reverse bits of a given 32 bits unsigned integer.
"""


def reverseBits(n: int) -> int:
    binary = bin(n).replace("0b", "")
    n = len(binary)

    buffer = []
    if n < 32:
        for i in range(0, 32 - n):
            buffer.append(0)

    rev = binary[::-1] + "".join(buffer)

    return int(rev, 2)

