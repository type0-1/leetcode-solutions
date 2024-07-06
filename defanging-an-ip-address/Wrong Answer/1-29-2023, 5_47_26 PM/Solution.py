// https://leetcode.com/problems/defanging-an-ip-address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = ""
        for i in address:
            if address != ".":
                s += i
            else:
                s += "[" + i + "]"
        return s