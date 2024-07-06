// https://leetcode.com/problems/unique-morse-code-words

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = "abcdefghijklmnopqrstuvwxyz"
        zipped = zip(alpha, morse)
        letters = {k : v for k, v in zipped}
        amount = []
        for word in words:
            s = ""
            for l in word:
                if l in letters:
                    s += letters[l]
            if s not in amount:
                amount.append(s)
        return len(amount)