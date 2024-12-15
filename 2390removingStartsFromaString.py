"Stack approach 1"
class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in s:
            res.append(i)
            if i == "*":
                res.pop()
                res.pop()
        return ''.join(res)
    
"Stack approach 2"
'''
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
'''
