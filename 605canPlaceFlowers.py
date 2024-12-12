class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # 이전 구역이 비어 있거나 경계를 벗어나는지 확인
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                # 다음 구역이 비어 있거나 경계를 벗어나는지 확인
                next_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    # 여기 꽃을 심습니다
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n <= 0