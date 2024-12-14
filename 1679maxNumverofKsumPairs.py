from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()  # 배열을 정렬합니다.
        l = 0
        r = len(nums) - 1
        oper = 0
        
        while l < r:
            if nums[l] + nums[r] == k:
                oper += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        return oper