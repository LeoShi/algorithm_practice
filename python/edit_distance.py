'''
TAG: Google
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2:
            return 0
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l1 + 1) for _ in range(l2 + 1)]
        for i in range(l1 + 1):
            dp[0][i] = i
        for j in range(l2 + 1):
            dp[j][0] = j

        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[l2][l1]

# print Solution().minDistance('abcd', 'bcaa')
print Solution().minDistance('abc', 'abd')