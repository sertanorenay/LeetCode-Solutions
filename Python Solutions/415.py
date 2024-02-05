class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        result = str()
        carry = 0
        for i in range(max(len(num1), len(num2))):
            a = int(num1[i]) if i < len(num1) else 0
            b = int(num2[i]) if i < len(num2) else 0
            result += str((a+b+carry) % 10)
            carry = 1 if (a+b+carry) > 9 else 0
        if carry: result += '1'
        return result[::-1]