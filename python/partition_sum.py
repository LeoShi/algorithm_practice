class Solution(object):
    '''
    https://leetcode.com/problems/partition-equal-subset-sum/description/
    
    Given a non-empty array containing only positive integers, 
    find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
    '''
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)

        def find(num, idx, temp):
            if idx >= len(nums):
                return
            if sum(temp) == num:
                return temp
            for i in range(idx, len(nums)):
                ret = find(num, i + 1, temp + [nums[i]])
                if ret:
                    return ret

        def yet_find(num):
            dp = [[0] * (num + 1) for _ in range(len(nums) + 1)]
            dp[0][0] = 1
            for i in range(1, len(nums) + 1):
                for j in range(num + 1):
                    if j - nums[i - 1] >= 0:
                        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                    else:
                        dp[i][j] = dp[i - 1][j]
            return dp[len(nums)][num]

        def backtracing_find(num, temp, visited):

            if sum(temp) == num:
                return temp

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    ret = find(num, temp + [nums[i]], visited)
                    visited[i] = False
                    if ret:
                        return ret

        if s % 2 != 0:
            return False
        # ret = find(s / 2, 0, []) or []
        ret = yet_find(s / 2) or []
        return ret > 0


# print Solution().canPartition([1,5,11,5])
print Solution().canPartition([1,2,5])
# print Solution().canPartition([1,2, 3, 5])
# print Solution().canPartition([100,100,100,100,100,100,100,100])