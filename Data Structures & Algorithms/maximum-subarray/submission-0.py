class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        run_sum = 0
        for i in range(len(nums)):
            if run_sum < 0:
                run_sum = 0
            run_sum += nums[i]
            max_sum = max(max_sum, run_sum)

        return max_sum
        