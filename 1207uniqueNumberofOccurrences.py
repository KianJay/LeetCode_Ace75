class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic1 = {}
        for i in arr:
            dic1[i] = dic1.get(i, 0) + 1
        dicSet = set()
        
        for value in dic1.values():
            if value in dicSet:
                return False
            dicSet.add(value)
        return True