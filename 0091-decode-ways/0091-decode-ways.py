class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n=len(s)
        f,g=0,1
        for i in range(1,n+1):
            h=0
            if s[i-1] != '0':
                h+=g
            
            if i>1 and s[i-2] != '0' and int(s[i-2:i]) <=26:
                h+=f
            f,g=g,h
        return g