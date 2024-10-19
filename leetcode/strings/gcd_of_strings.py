import math


def gcdOfStrings(self, str1: str, str2: str) -> str:
    def isDivisible(s1, s2):
        return s1 == s2 * (len(s1) // len(s2))

    gcd_length = math.gcd(len(str1), len(str2))

    candidate = str1[:gcd_length]

    if isDivisible(str1, candidate) and isDivisible(str2, candidate):
        return candidate
    else:
        return ""
