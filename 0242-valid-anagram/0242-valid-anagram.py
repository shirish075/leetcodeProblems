class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(i for i in s)
        b=list(i for i in t)
        a.sort()
        b.sort()
        if a==b:
            return True
        else:
            return False
        return a==b
