class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sums = [0]
        
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
        
        answer = []
        for query in queries:
            left, right = 0, len(prefix_sums) - 1
            while left <= right:
                mid = (left + right) // 2
                if prefix_sums[mid] <= query:
                    left = mid + 1
                else:
                    right = mid - 1
            answer.append(right)
        
        return answer
