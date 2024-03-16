class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        modified = t
        for i in range(len(s)):
            if s[i] in t:
                modified = modified.replace(s[i], '', 1)
        return len(modified) == 0
