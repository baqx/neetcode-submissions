class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        result = True
        if len(s) == len(t):
            for letter in t:
                if letter in s:
                    result = True
                    s.remove(letter)
                else:
                    result = False
                    break
        else:
            result = False
        return result