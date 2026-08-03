class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)

        dp = [-10**18] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):

            take = 0

            for k in range(3):

                if i + k >= n:
                    break

                take += stoneValue[i + k]

                dp[i] = max(
                    dp[i],
                    take - dp[i + k + 1]
                )

        if dp[0] > 0:
            return "Alice"

        if dp[0] < 0:
            return "Bob"

        return "Tie"