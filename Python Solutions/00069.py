class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        min = 1
        max = x // 2

        while min <= max:
            mid = (max + min) // 2
            if mid * mid > x:
                max = mid - 1
            else:
                min = mid + 1
        return max