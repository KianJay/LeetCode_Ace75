class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_alt = 0
        max_alt = 0
        for i in range(0,len(gain)):
            cur_alt += gain[i]
            max_alt = max(max_alt, cur_alt)
        return max_alt
        