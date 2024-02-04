class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        num = x // 2
        while num * num > x:
            num -= 1
        return num
    """
    TIME LIMIT
    """