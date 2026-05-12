class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        maximum = 0
        number = None
        for key, item in counts.items():
            if maximum <= item:
                number = key
                maximum = item
        return number