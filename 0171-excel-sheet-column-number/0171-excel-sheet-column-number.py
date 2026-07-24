class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        i = len(columnTitle) - 1
        pow_26 = 1
        ans = 0
        
        
        while i >= 0:
            ascii_val = ord(columnTitle[i])
            val = ascii_val - 64
            ans += val * pow_26
            pow_26 *= 26
            i -= 1
        
        
        return ans