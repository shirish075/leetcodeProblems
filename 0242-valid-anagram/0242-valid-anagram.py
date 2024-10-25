class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(i for i in s)
        b=list(i for i in t)
        a.sort()
        b.sort()
        return a==b
