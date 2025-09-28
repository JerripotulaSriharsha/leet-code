class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = {n for n in nums if n > 0}
        return 1 if not s or min(s) > 1 else next(x for x in range(1, len(s)+2) if x not in s)
