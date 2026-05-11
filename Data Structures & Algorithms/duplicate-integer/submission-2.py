class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l1 = len(nums)
        l2 = len(set(nums))

        return False if l1 == l2 else True