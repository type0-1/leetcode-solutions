// https://leetcode.com/problems/fizz-buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 != 0:
                results.append("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                results.append("Buzz")
            elif i % 3 == 0 and i % 5 == 0:
                results.append("FizzBuzz")
            else:
                results.append(str(i))
        return results
