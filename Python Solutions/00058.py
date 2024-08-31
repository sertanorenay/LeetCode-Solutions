class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        index = -1
        while words[index] == ' ':
            index -= 1
        return len(words[index])