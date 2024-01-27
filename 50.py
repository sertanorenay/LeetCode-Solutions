class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        result = 1
        for _ in range(abs(n)):
            result *= x
        return result if n > 0 else 1 / result
    """
    TIME LIMIT
    """