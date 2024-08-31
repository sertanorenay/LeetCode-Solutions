class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []
        for i in range(len(s)):
            if s[i].isalpha():
                letters.append(s[i].lower())
        
        length = len(letters)
        for i in range(length//2):
            if letters[i] != letters[length - 1 - i]:
                return False
        return True