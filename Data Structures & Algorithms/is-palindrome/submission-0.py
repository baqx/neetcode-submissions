class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        cleaned_s = "".join(char for char in s if char.isalnum())
        reverse_s = "".join(reversed(cleaned_s))
        if reverse_s == cleaned_s:
            return True
        else: 
            return False