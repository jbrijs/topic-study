from typing import List

'''
Leetcode #412 - Fizz Buzz

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
'''

def fizzBuzz(self, n: int) -> List[str]:
        res = []
        
        for i in range(n):
            answer = ""
            if (i + 1) % 3 == 0:
                answer += "Fizz"
            if (i + 1) % 5 == 0:
                answer += "Buzz"
            elif len(answer) == 0:
                answer += str(i + 1)
            res.append(answer)

        return res