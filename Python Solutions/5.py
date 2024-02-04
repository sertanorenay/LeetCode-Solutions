class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for start in range(len(s)):
            for end in range(start, len(s)):
                sub = s[start:end+1]
                if sub == sub[::-1] and len(sub) > len(longest):
                    longest = sub
        return s if longest == '' else longest
    """
    HIGH RUN TIME COMPLEXITY
    """