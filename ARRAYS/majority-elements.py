from collections import Counter 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts  = Counter(nums)
        sorted_counts = counts.most_common()
        return sorted_counts[0][0]