class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        keyva={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s) - 1):
            if keyva[s[i]] >= keyva[s[i + 1]]:
                num += keyva[s[i]]
            else:
                num -= keyva[s[i]]
        num += keyva[s[-1]]
        return num
        