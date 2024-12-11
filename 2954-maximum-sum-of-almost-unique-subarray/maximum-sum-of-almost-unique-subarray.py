class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        max_sum = 0
        current_sum = 0
        window_count = Counter()
        distinct_count = 0

        for i in range(k):
            num = nums[i]
            current_sum += num
            if window_count[num] == 0:
                distinct_count += 1
            window_count[num] += 1

        if distinct_count >= m:
            max_sum = max(max_sum, current_sum)

        for i in range(k, n):
            out_num = nums[i - k]
            current_sum -= out_num
            window_count[out_num] -= 1
            if window_count[out_num] == 0:
                distinct_count -= 1

            in_num = nums[i]
            current_sum += in_num
            if window_count[in_num] == 0:
                distinct_count += 1
            window_count[in_num] += 1

            if distinct_count >= m:
                max_sum = max(max_sum, current_sum)

        return max_sum