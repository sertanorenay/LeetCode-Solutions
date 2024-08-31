class Solution:
    def firstUniqChar(self, s: str) -> int:
        set1, set2 = set(), set()
        for ch in s:
            if ch in set1:
                set2.add(ch)
            else: 
                set1.add(ch)
        for i, ch in enumerate(s):
            if ch not in set2:
                return i
        return -1