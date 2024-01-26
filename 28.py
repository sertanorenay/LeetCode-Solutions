class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len1, len2 = len(haystack), len(needle)
        for start in range(len1):
            if haystack[start : start + len2] == needle:
                return start
        return -1