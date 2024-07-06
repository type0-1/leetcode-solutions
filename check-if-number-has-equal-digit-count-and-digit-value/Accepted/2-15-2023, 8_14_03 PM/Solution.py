// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value

class Solution:
    def digitCount(self, num: str) -> bool:
        check = "".join([str(i) for i in range(len(num))])
        final = []
        for i in check:
            final.append(str(num.count(i)))
        compare = "".join(final)
        return compare == num