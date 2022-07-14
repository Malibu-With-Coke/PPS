class Solution(object):
    def generate(self, numRows):
        dp = []
        for i in xrange(numRows):
            tmp = [1] * (i+1)
            dp.append(tmp)
            for j in xrange(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        return dp
