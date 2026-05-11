class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}

        # Count frequency
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        # Sort by frequency descending
        sorted_items = sorted(
            counts.items(),
            key=lambda item: item[1],
            reverse=True
        )

        result = []

        # Take first k elements
        for i in range(k):
            result.append(sorted_items[i][0])

        return result