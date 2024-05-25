class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        num_list = list(num)

        def next_permutation(arr):
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            if i == -1:
                return False
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1:] = reversed(arr[i + 1:])
            return True

        for _ in range(k):
            next_permutation(num_list)

        kth_permutation = ''.join(num_list)

        num_list = list(num)
        kth_list = list(kth_permutation)

        swaps = 0
        for i in range(len(num_list)):
            if num_list[i] != kth_list[i]:
                j = i
                while num_list[j] != kth_list[i]:
                    j += 1

                while j > i:
                    num_list[j], num_list[j - 1] = num_list[j - 1], num_list[j]
                    swaps += 1
                    j -= 1

        return swaps
