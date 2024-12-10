class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_divisible(s1, s2):
            return s1 == s2 * (len(s1) // len(s2))
        
        res = ""
        for i in range(len(str2), 0, -1):
            candidate = str2[:i]
            if is_divisible(str1, candidate) and is_divisible(str2, candidate):
                return candidate
        return ""