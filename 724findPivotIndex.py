class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            # 오른쪽 합은 전체 합에서 현재 인덱스의 값과 왼쪽 합을 뺀 값
            right_sum = total_sum - left_sum - nums[i]
            
            if left_sum == right_sum:
                return i
            
            left_sum += nums[i]
        
        return -1