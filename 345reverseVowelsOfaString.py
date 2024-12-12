class Solution:
    def reverseVowels(self, s: str) -> str:
        vows = "aeiouAEIOU"
        v = []
        s_list = list(s)
        for ch in s:
            if ch in vows:
                v.append(ch)
        v.reverse()

        v_index = 0
        for i in range(len(s_list)):
            if s_list[i] in vows:
                s_list[i] = v[v_index]
                v_index+=1
        return ''.join(s_list)

"""
Two pointer
class Solution:
    def reverseVowels(self, s: str) -> str:
        vows = "aeiouAEIOU"
        s_list = list(s)  # 문자열을 리스트로 변환하여 수정 가능하게 함
        left, right = 0, len(s) - 1
        
        while left < right:
            # 왼쪽 포인터가 모음을 가리킬 때까지 이동
            while left < right and s_list[left] not in vows:
                left += 1
            # 오른쪽 포인터가 모음을 가리킬 때까지 이동
            while left < right and s_list[right] not in vows:
                right -= 1
            
            # 두 모음을 교환
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        
        return ''.join(s_list)
"""