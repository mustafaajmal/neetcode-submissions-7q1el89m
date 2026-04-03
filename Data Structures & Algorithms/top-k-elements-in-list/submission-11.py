from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_nums = sorted(list(Counter(nums).items()), key=lambda x: x[1], reverse=True)
        top_k_frequent = []
        for i in range(k):
            top_k_frequent.append(counted_nums[i][0])
        return top_k_frequent