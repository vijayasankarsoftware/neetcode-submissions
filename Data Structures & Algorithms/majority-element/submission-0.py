class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        m = 0
        majority = 0
        for key, item in count.items():
            if m < item:
                m = item
                majority = key
        return majority
