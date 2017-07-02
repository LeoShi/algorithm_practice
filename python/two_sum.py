#Two sum: https://leetcode.com/problems/target-sum/#/description

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def find(n, nums, sum):
            if n == len(nums):
                return 1 if sum == 0 else 0
            return find(n + 1, nums, sum + nums[n]) + find(n + 1, nums, sum - nums[n])

        return find(0, nums, S)

    def dp_2d(self, nums, S):
        s = sum(nums)

        dp = [[0] * (2 * s + 1) for _ in range(len(nums) + 1)]
        dp[0][s] = 1
        for i in range(1, len(nums) + 1):
            for j in range(2 * s + 1):
                if j + nums[i - 1] <= 2 * s:
                    dp[i][j] += dp[i - 1][j + nums[i - 1]]
                if j - nums[i - 1] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
        print dp

        return dp[len(nums)][s + S]

    def dp_1d(self, nums, S):
        from collections import defaultdict

        dp = {0: 1} # how many possible combo to reach to some val k, where k is the key of dic
        for item in nums:
            tmp = defaultdict(int)
            for item_count, ways in dp.items():
                tmp[item_count + item] += ways
                tmp[item_count - item] += ways
            dp = tmp
        print dp
        return dp[S]


print Solution().findTargetSumWays([1,1,1,1,1], 3)
print Solution().dp_2d([1,1,1,1,1], 3)
print Solution().dp_1d([1,1,1,1,1], 3)