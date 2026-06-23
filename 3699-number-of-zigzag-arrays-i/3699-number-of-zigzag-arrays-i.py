class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        r -= l
        dp = [1] * (r + 1)
        for i in range(1, n):
            pre = 0
            if i & 1:
                for v in range(r + 1):
                    pre, dp[v] = (pre + dp[v]) % MOD, pre
            else:
                for v in range(r, -1, -1):
                    pre, dp[v] = (pre + dp[v]) % MOD, pre
        return sum(dp) % MOD * 2 % MOD