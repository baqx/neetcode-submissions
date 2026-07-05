class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        noOfWords = len(arr[len(arr)-1])
        return noOfWords