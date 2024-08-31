class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        arr = []

        for char in s:
            if char.lower() in vowels:
                arr.append(char)
        arr.reverse()

        new_str = str()
        index = 0
        for char in s:
            if char.lower() in vowels:
                new_str += arr[index]
                index += 1
            else:
                new_str += char   
        return new_str